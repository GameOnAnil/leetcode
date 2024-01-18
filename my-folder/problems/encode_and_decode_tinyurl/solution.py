import re

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        first= re.split(r'(?<!/)/(?!/)', longUrl)[0]+"/"
        second= longUrl.split(first)[1]
        second.encode("utf-8")
        return first+second
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        first= re.split(r'(?<!/)/(?!/)', shortUrl)[0]+"/"
        second= shortUrl.split(first)[1]
        s= bytes(second, 'utf-8')
        decoded = s.decode("utf-8")
        return first+decoded
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))