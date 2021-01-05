class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.isV4(IP):
            return 'IPv4'
        if self.isV6(IP):
            return 'IPv6'
        return 'Neither'

    def isV4(self, IP: str) -> str:
        segments = IP.split('.')
        if len(segments) != 4:
            return False
        for idx, segment in enumerate(segments):
            if len(segment) > 1 and segment[0] == '0':
                return False
            if not segment.isnumeric() or not (0 <= int(segment) <= 255):
                return False
        return True

    def isV6(self, IP: str) -> None:
        segments = IP.split(':')
        if len(segments) != 8:
            return False
        for idx, segment in enumerate(segments):
            if not (1 <= len(segment) <= 4):
                return False
            try:
                int(segment, 16)
            except ValueError:
                return False
        return True

