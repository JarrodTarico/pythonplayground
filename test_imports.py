# whenever you import a file, python runs the code in that file, thats
# why __name__ variable will be the the name of the file and not __main__
# now if python is running a file directly __name__ == '__main__'
# This way you can run code you only want to run if the file is being ran directly
#  
import asyncio_playground

async def main():
    result = await asyncio_playground.find_divisibles(100, 99)
    print (result)