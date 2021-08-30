import asyncio

#Note: Adding async infront of a function makes it a coroutine
async def find_divisibles(inrange: int, div_by: int):
    print ("The numbers in the range 0 to {} are divisble by {}".format(inrange, div_by))
    located: list = []
    for i in range(inrange):
        if i % div_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.0001)
    print (("For input {} and {} here are the numbers {}".format(inrange, div_by, located)))


async def main():
    divs1 = loop.create_task(find_divisibles(3423, 2))
    divs2 = loop.create_task(find_divisibles(50, 9))
    divs3 = loop.create_task(find_divisibles(800, 4))
    #runs this as a batch
    await asyncio.wait([divs1,divs2,divs3])


if __name__ == '__main__':
    #we want to run the main coroutine until complete
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except Exception as e:
        print (e)
    finally:
        loop.close()
