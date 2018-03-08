from subprocess import call
from subprocess import check_call
from subprocess import CalledProcessError, STDOUT
import os

class PgpHelper(object):

  # Encrypt a file.
  def encryptFile(self, recipient, toBeEncryptedFilepath, outputFilepath):
    # Call gpg command line to encrypt the file.
    returnCode = 0
    try:
      check_call(["gpg",
      "--batch",
      "--yes",
      "--no-secmem-warning",
      "--armor",
      "--trust-model", "always",
      "--output", outputFilepath,
      "--recipient", recipient,
      "--encrypt", toBeEncryptedFilepath])
      # Check for error code.
      print("\"%s\" has been encrypted to \"%s\"." % (toBeEncryptedFilepath, outputFilepath))
    except CalledProcessError as errCode:
      print("Encrypting file has failed with error code is %d.\n" % (errCode.returncode))
      returnCode = errCode.returncode
    return returnCode


  # Handle gpg encryption when the output filename is the same as the input filename.
  def encryptFileSameName(self, recipient, toBeEncryptedFilepath):
    temp = 'temp.temp'
    returnCode = 0
    returnCode = self.encryptFile(recipient, toBeEncryptedFilepath, temp)
    writer = open(toBeEncryptedFilepath, 'w')
    reader = open(temp, 'r')
    writer.write(reader.read())
    writer.close()
    reader.close()
    # os.remove(temp)
    return returnCode


  # Decrypt an encrypted file.
  def decryptFile(self, passphrase, encryptedFilepath, outputFilepath):
    # Call gpg command line to decrypt the file.
    returnCode = 0
    try:
      check_call(["gpg",
      "--batch",
      "--yes",
      "--no-secmem-warning",
      "--no-mdc-warning",
      "--output", outputFilepath,
      "--passphrase", passphrase,
      "--decrypt", encryptedFilepath])
      # Check for error code.
      print("\"%s\" has been decrypted to \"%s\"." % (encryptedFilepath, outputFilepath))
    except CalledProcessError as errCode:
      print("Decrypting file has failed with error code is %d.\n" % (errCode.returncode))
      returnCode = errCode.returncode
    return returnCode


  # Add Vantiv public key into merchants' keyrings.
  def importVantivPublicKey(self, publicKeyFilePath):
    # Call gpg command line to import public key.
    try:
      check_call(["gpg",
      "--import", publicKeyFilePath])
      #Check for error code.
      print("Successfully added Vantiv public key!")
    except CalledProcessError as errCode:
      print("Adding Vantiv public key has failed with error code is %d.\n" % (errCode.returncode))

