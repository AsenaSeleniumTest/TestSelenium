from EncriptionTypes import encript_object 
import hashlib

class Testclass:
    def test_encription():
        result =  encript_object('test','sha256')
        assert result is hashlib.sha3_256