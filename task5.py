class RFIDBlocker:
    def __init__(self, blocked_tags=[]):
        self.blocked_tags = blocked_tags

    def add_blocked_tag(self, tag):
        self.blocked_tags.append(tag)

    def remove_blocked_tag(self, tag):
        if tag in self.blocked_tags:
            self.blocked_tags.remove(tag)

    def is_tag_blocked(self, tag):
        return tag in self.blocked_tags


# Example Usage
if __name__ == "__main__":
  
    rfid_blocker = RFIDBlocker()
    rfid_blocker.add_blocked_tag("CreditCardRFID")
    rfid_blocker.add_blocked_tag("PassportRFID")
    tag_to_check = "CreditCardRFID"
    if rfid_blocker.is_tag_blocked(tag_to_check):
        print(f"{tag_to_check} is blocked!")
    else:
        print(f"{tag_to_check} is not blocked.")
    rfid_blocker.remove_blocked_tag("CreditCardRFID")
    if rfid_blocker.is_tag_blocked(tag_to_check):
        print(f"{tag_to_check} is still blocked!")
    else:
        print(f"{tag_to_check} is not blocked anymore.")
