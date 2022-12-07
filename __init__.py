from binaryninja import *
from binaryninjaui import DockHandler, DockContextHandler, UIActionHandler, getMonospaceFont

HOOKED_HAL_ADDR = {'samr21_http.elf': [0x969e, 0x8b1c, 0x8bb0, 0x348c, 0x3358, 0x80c0, 0x19fc, 0x187c, 0x122c, 0x1520, 0x488, 0x7c90, 0x81c4, 0x14f0, 0x6f94, 0x6f5c, 0x4494, 0x7ca8, 0x7cbc, 0x7cd0]}

def find_HAL_blocks(bv):
    filename = bv.file.filename.split('/')[-1]
    log.log(1, filename)
    for addr in HOOKED_HAL_ADDR[filename]:
        func = bv.get_function_at(addr)

        if func is None:
            log.log(2, "No function at {}".format(hex(addr)))
            return

        log.log(1, "{}".format(func))

        bbs = function.BasicBlockList(func)
        log.log(1, "{}".format(bbs))
        log.log(1, "num of basic blocks: {}".format(len(bbs)))
        log.log(1, "___________________________________")


# view.always_branch ,  view.convert_to_nop / never_branch, view.invert_branch, save
PluginCommand.register("HALextract\\Generate blacklist", "Generate a list of basic block contained in the HAL functions specified by hard-coded entry points", find_HAL_blocks)