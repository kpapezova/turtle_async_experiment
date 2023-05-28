# To try asynchronous programming
# My task - While the turtle is drawing regular n-sided polygons, their perimeter is calculated


import asyncio
from turtle import forward, left, right, exitonclick, penup, pendown

async def draw_polygons():
    '''This function draws polygons'''  
    print('start drawing')

    for n in range(3, 11):      # n - number of angles
        angle = 180 - (180 * (1-2/n))
        for _ in range(n):
            forward(200/n)
            left(angle)
        penup()
        forward(100)
        pendown()
        await asyncio.sleep(0.1)        # the function awaits given time and another async function is executed

    print('finish drawing')
    exitonclick()

async def count_perimeter():
    '''Function for calculating a perimeter of polygons'''
    length = 5
    unit = 'cm'
    for n in range(3, 11):
        perimeter = n * length
        print(f'Perimeter of {n}-sided regular polygon with length of the side {length} {unit} is {perimeter} {unit}')
        # await asyncio.sleep(0.1)

    

async def main():
    print('While the turtle is drawing regular n-sided polygons, their perimeter is calculated')
    task1 = asyncio.create_task(draw_polygons())
    task2 = asyncio.create_task(count_perimeter())
    await task1     # waits for drawing to finish
    print('finished')


asyncio.run(main())






## further extensions that can be done
# - length and unit as user input