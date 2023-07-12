

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '!help':
        return "@everyone DID SOMEONE SAY [Thunderfury, Blessed Blade of the Windseeker]!?!?"
    else:
        return "@everyone A triumphant roar echoes from atop the Seat of the Aspects as Nasz'uro, the Unbound Legacy is formed."