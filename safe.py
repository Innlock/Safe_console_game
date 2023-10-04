import random

def is_web():
    return "__BRYTHON__" in globals()

def write(message, end='\n'):
    if is_web():
        from browser import document
        console = document.getElementById('console')
        if len(message) == 0:
            p = document.createElement('br') # для отступов где пустые строки
        else:
            p = document.createElement('p')
            p.textContent = message
        console.appendChild(p)
        console.scrollTop = console.scrollHeight # автоматическая прокрутка к последнему добавленному сообщению
    else:
        print(message, end=end)


async def read():
    if is_web():
        from browser import document, aio
        inp = document.getElementById('input')
        while True:
            event = await aio.event(inp, 'keydown')
            if event.key == 'Enter':
                tmp = event.target.value # получение ввода
                event.target.value = '' # очищает поле ввода
                write(tmp)
                return tmp
    else:
        return input()


def run(function):
    if is_web():
        from browser import aio
        aio.run(function())
    else:
        import asyncio
        asyncio.run(function())


async def initialize():
    write(" " * 28 + "SAFE")
    write(" " * 20 + "CREATIVE CONFUTING")
    write(" " * 18 + "MORRISTOWN, NEW JERSEY")
    write("")
    write("")
    write("")

    while True:
        write("DO YOU WANT DIRECTIONS?", end=" ")
        input_value = await read()
        if input_value == "YES":
            await rules()
            break
        elif input_value != "NO":
            write("ANSWER YES OR NO")
        else:
            break
    await main()


async def rules():
    write("")
    write("YOU ARE A BURGLAR AND HAVE ENCOUNTERED A SAFE. YOU MUST")
    write("OPEN THE SAFE TO GET THE SECRET PLANS THAT YOU CAME FOR.")
    write("TO DO THIS, YOU MUST ENTER THE NUMBER OF WHAT YOU WANT THE")
    write("DIAL TURNED TO. THE COMPUTER WILL ACT AS THE SAFE AND WILL")
    write("HELP YOU BY GIVING A SORT OF CLUE. YOU WILL 'HEAR' A CLICK")
    write("AT EVENLY SPACED NOTCHES AS YOU MOVE TO THE PROPER NUMBER.")
    write("THERE ARE FOUR OF THEM BEFORE THE FINAL CLICK IS 'HEARD'.")
    write("AFTER THE FINAL ONE IS HEARD, YOU WILL GO ON TO THE NEXT NUMBER.")
    write("THE COMPUTER WILL 'SAY' 'CLICK' FOR EACH NOTCH THAT YOU PASS")
    write("AND '**CLICK**' WHEN YOU REACH THE PROPER NUMBER.")
    write("IF YOU PASS IT OR TAKE LONGER THAN TEN TRIES ON ANY ONE NUMBER,")
    write("YOU WILL ACTIVATE THE ALARM.")
    write("REMEMBER THAT WHEN YOU TURN THE DIAL TO THE LEFT, THE NUMBERS")
    write("GO FROM 1 - 99, AND WHEN YOU GO TO THE RIGHT, THE NUMBERS GO")
    write("FROM 99 - 1")
    write("")


async def defeat():
    write("THE SENSOR HAS BEEN TRIGGERED")
    write("LEAVE WHILE YOU CAN BEFORE THE POLICE GET HERE.")
    write("WANT TO TRY THE SAME SAFE?", end=" ")
    input_value = await read()
    if input_value == "YES":
        return True
    return False


def generate_numbers():
    A1 = [0] * 5
    A, B, C = 0, 0, 0
    while not (A > B and C > B):
        A = int(random.random() * 81 + 10)
        B = int(random.random() * 81 + 10)
        C = int(random.random() * 81 + 10)
    return (A, B, C), A1


async def main():
    continue_game = True
    while continue_game:
        numbers, A1 = generate_numbers()
        continue_game = await game_loop(True, numbers, A1)


async def game_loop(retry, numbers, A1):
    while retry:
        retry = await start_game(numbers, A1)
        if retry is None:
            return False
    return True


async def start_game(numbers, A1):
    A, B, C = numbers
    write("OKAY, START TO THE RIGHT, SHHHHHH!!!!!!!!!!!!!!")

    write("ARE YOU READY?", end=" ")
    input_value = await read()
    if input_value == "WHAT":
        write(f"{A} {B} {C}")
    elif input_value != "YES":
        return None

    L = 100 - A
    for M in range(1, 5):
        A1[M] = (5 - M) * L / 5 + A

    J = 1
    write("OKAY, THEN LET'S START")
    while True:
        M = int(await read())
        if M < A:
            return await defeat()
        elif M > A:
            for K in range(1, 5):
                if M < A1[K]:
                    write("CLICK")
            if J >= 10:
                return await defeat()
            J += 1
        else:
            write("**CLICK**")
            break

    L = L + B
    for K in range(1, 5):
        A1[K] = K * L / 5 + B

    write("AND NOW TO THE LEFT")

    J = 1
    while True:
        M = int(await read())
        if M == A or A > M > B:
            return await defeat()
        if M < A:
            if M == B:
                write("**CLICK**")
                break
            else:
                M += 100

        for K in range(1, 5):
            if M >= A1[K]:
                write("CLICK")
                A1[K] = 200
        if J >= 10:
            return await defeat()
        J += 1

    L = (100 - C) + B
    for K in range(1, 5):
        A1[K] = B + 100 - K * L / 5

    write("AND NOW TO THE RIGHT AGAIN")

    J = 1
    while True:
        M = int(await read())
        if M == B or B < M < C:
            return await defeat()
        if M > B:
            if M == C:
                write("**CLICK**...YOU OPENED IT")
                break
        else:
            M += 100

        for K in range(1, 5):
            if M <= A1[K]:
                write("CLICK")
                A1[K] = -200
        if J >= 10:
            return await defeat()
        J += 1

    write("BUT OH, OH, HE MUST HAVE MOVED IT")
    write("TRY THE ONE OVER THERE")
    return False



run(initialize)