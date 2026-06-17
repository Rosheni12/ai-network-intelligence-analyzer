class IPSanitizer:
    def __init__(self):
        self.ip_map = {}
        self.counter = 1

    def sanitize(self, ip):
        """
        Converts real IP → Client_1, Client_2, etc.
        Keeps mapping consistent during runtime.
        """

        if ip not in self.ip_map:
            self.ip_map[ip] = f"Client_{self.counter}"
            self.counter += 1

        return self.ip_map[ip]