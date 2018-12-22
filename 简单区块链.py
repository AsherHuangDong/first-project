import hashlib
import datetime

class DongBlockcoin(object):
    def __init__(self, index, data, pre_hash):
        self.index = index
        self.data = data
        self.time = datetime.datetime.now()
        self.hash = self.GetHash()
        self.pre_hash = pre_hash

    def GetHash(self):
        sha = hashlib.md5()
        sha.update((str(self.index) + str(self.time) + str(self.data)).encode("utf-8"))
        return sha.hexdigest()

def create_first_Biock():
    return DongBlockcoin(0, "jam is a good man", '0')


def create_next_Block(last_Block):
    this_index = last_Block.index + 1
    this_data = 'lovaDongcoin' + str(this_index)
    this_hash = last_Block.hash
    return DongBlockcoin(this_index, this_data, this_hash)

dongblockcoins = [create_first_Biock()]
num=20
head_block = dongblockcoins[0]
print(head_block.index, head_block.hash, head_block.pre_hash, head_block.data, head_block.time)
for i in range(num):
    dongblock_add = create_next_Block(head_block)
    dongblockcoins.append(dongblock_add)
    head_block = dongblock_add
    print(dongblock_add.index, dongblock_add.hash, dongblock_add.pre_hash, dongblock_add.data, dongblock_add.time)