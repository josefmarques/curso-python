# chapar pao
# fritar hamburger
# montar sanduiche
# fazer milkshake

from time import sleep
import asyncio    
        
        
# class SyncSpongeBob:
#     def cook_bread(self):
#         sleep(3)

#     def cook_hamburger(self):
#         sleep(10)

#     def mount_sanduiche(self):
#         sleep(3)

#     def make_milkeshake(self):
#         sleep(5)
        
#     def cook(self):
#         self.cook_bread()
#         self.cook_hamburger()
#         self.mount_sanduiche()
#         self.make_milkeshake()
        
# sync_spongebob = SyncSpongeBob()
# sync_spongebob.cook()


class AsyncSpongeBob:

    async def cook_bread(self):
        await asyncio.sleep(3)

    async def cook_hamburger(self):
        await asyncio.sleep(10)

    async def mount_sanduiche(self):
        await asyncio.sleep(3)

    async def make_milkeshake(self):
        await asyncio.sleep(5)
        
    async def cook(self):
        await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburger(),            
            self.make_milkeshake()
        )
        await self.mount_sanduiche()


async_spongebob = AsyncSpongeBob()
asyncio.run(async_spongebob.cook())