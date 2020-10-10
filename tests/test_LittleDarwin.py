import os
import shutil
import sys
import unittest
import tempfile
import base64
import zipfile
from io import BytesIO

from littledarwin import LittleDarwin


class TestLittleDarwin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.videostoreZipContentBase64 = b'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'
        cls.videostoreZipContent = BytesIO(base64.decodebytes(cls.videostoreZipContentBase64))

    def setUp(self) -> None:
        self.tempDir = tempfile.TemporaryDirectory()
        self.videoStoreSourcePath = os.path.join(self.tempDir.name, "videostore", "src", "main")
        self.videoStoreBuildPath = os.path.join(self.tempDir.name, "videostore")

        print("Created temp directory: " + str(self.tempDir.name) + ".")

        zipObj = zipfile.ZipFile(self.videostoreZipContent)
        zipObj.extractall(path=self.tempDir.name)
        print("Extracted \"VideoStore\" project.")

    def tearDown(self) -> None:
        self.tempDir.cleanup()
        print("Deleted temp directory.")

    def test_VideoStoreGenerateTraditionalMutants(self):
        argList = ['-m', '-p', self.videoStoreSourcePath, '-t', self.videoStoreBuildPath]
        print("Running LittleDarwin with arguments:\n" + " ".join(argList))

        try:
            sys.exit(LittleDarwin.main(argList))

        except Exception as e:
            print(e)
            self.fail("Irregular exit: exception occured.")

        except SystemExit as e:
            self.assertEqual(int(e.code), 0)

    def test_VideoStoreTraditionalBuild(self):
        mavenPath = shutil.which("mvn")
        if mavenPath is None:
            mavenPath = shutil.which("mvn.bat")

        if mavenPath is None:
            mavenPath = shutil.which("mvn.cmd")

        self.assertIsNotNone(mavenPath)

        argList = ['-m', '-b', '-p', self.videoStoreSourcePath, '-t', self.videoStoreBuildPath, '-c',
                   str(mavenPath) + ",clean,test"]
        print("Running LittleDarwin with arguments:\n" + " ".join(argList))

        try:
            sys.exit(LittleDarwin.main(argList))

        except Exception as e:
            print(e)
            self.fail("Irregular exit: exception occured.")

        except SystemExit as e:
            self.assertEqual(int(e.code), 0)


if __name__ == '__main__':
    unittest.main()
