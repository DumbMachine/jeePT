questions = [
    {
        "text": """The equation of wave is given as y = 0.05 sin(2𝑥 − 4𝑡), where 𝑥 in meters and 𝑡 is time in seconds. The velocity of the wave is equal to""",

         "option": ["""2""",
         """4""",
         """0.5""",
         """0.25"""],
        "answer": "A",
    },
    {
        "text": """Two charges 𝑞1 and 𝑞2 separated by a distance 𝑑 are placed in a medium of dielectric constant 𝑘, if they are placed in the air then find equivalent distance at which they experience same force.""",
         "option": ["""𝑑√𝑘""",
         """𝑘√𝑑""",
         """2𝑑√𝑘""",
         """1.5𝑑√𝑘"""],
        "answer": "A",
    },
    {
        "text": """In the circuit shown, Find the current through 𝑅4(𝐼4) and 𝑅5(I5)""",
         "option": ["""I4=(24/55)A,I5=(96/55)A""",
         """I4=(96/55)A,I5=(24/55)A""",
         """I4=(24/37)A,I5=(96/37)A""",
         """I4=(96/37)A,I5=(24/37)A"""],
        "answer": "A",
    },
    {
        "text": """A circular loop of radius 10 𝑐𝑚 is placed in a linearly varying perpendicular magnetic field which has magnitude √𝜋 0.5 𝑇 at time 𝑡 = 0. The magnetic field reduces to zero at 𝑡 = 0.5 𝑠𝑒𝑐. Find the 𝑒𝑚𝑓 induced in the loop at 𝑡 = 0.25 𝑠𝑒𝑐.""",
         "option": ["""0.01 𝑉""",
         """0.005 𝑉""",
         """0.02 𝑉""",
         """0.03 𝑉"""],
        "answer": "A",
    },
    {
        "text": """If a ball is thrown from ground in vertical plane, it attains maximum height of 360 𝑚. Find the maximum distance, the ball can cover on ground keeping the projection speed constant.""",
         "option": ["""360𝑚""",
         """720𝑚""",
         """1440 𝑚""",
         """180𝑚"""],
        "answer": "B",
    },
    {
        "text": """Which statement is correct about photoelectric effect?""",
         "option": ["""Maximum kinetic energy depends upon intensity of light.""",
         """Stopping potential is dependant only on work function of metal.""",
         """Photoelectric effect can be explained by wave nature of light.""",
         """Photoelectric effect can be explained by particle nature of light."""],
        "answer": "D",
    },
    {
        "text": """Two parallel infinite wires carry equal currents are arranged parallel to each other with same direction of current. If both the currents are doubled and separation is halved, the force on a 10 𝑐𝑚 section of one of the wires becomes:""",
         "option": ["""4 times""",
         """1/4 times""",
         """8 times""",
         """1/8 times"""],
        "answer": "C",
    },
    {
        "text": """Statement 1: Photodiodes are operated in reverse biased. Statement 2 : Current in forward biased is more than current in reverse bias in 𝑝 − 𝑛 diode.""",
         "option": ["""Both the statements are true.""",
         """Statement 1 is true and statement 2 is false.""",
         """Statement 1 is true and statement 2 is false.""",
         """Both the statements are false."""],
        "answer": "A",
    },
    {
        "text": """Weight of an object at earth’s surface is 18 𝑁. If the object is taken 3200 𝑘𝑚 above the surface, then the weight of the object (in 𝑁) is_______ .(Given; radius of Earth =6400 𝑘𝑚)""",
        "option": [],
        "answer": "8",
    },
    {
        "text": """Statement 1: If the weight of the lift is equal to the tension force of the cable wire, then it moves with uniform velocity. Statement 2: If the lift moves downward with an acceleration, then the contact force between the boy’s feet and lift floor is more than the weight of boy.""",
         "option": ["""Both the statements are true and (2) is the correct explanation of (1)""",
         """Both the statements are true and (2) is not the correct explanation of (1)""",
         """Statement 1 is true and statement 2 is false.""",
         """Statement 2 is true and statement 1 is false."""],
        "answer": "C",
    },
]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
formatOption= lambda opt, idx: f'Option({alphabet[idx]}): {opt}'

for ques in questions:
    options = "\n".join([
        formatOption(opt, idx) for idx, opt in enumerate(ques["option"])
    ])

    prompt_ = f"""{ques['text']}\n{options}\nAnswer:{ques["answer"]}""".format(question=ques["text"])