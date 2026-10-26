import random
from typing import Generator


def gen_event() -> Generator[tuple[str,str],None,None]:
    names = ["Ballerina Cappuccina", "Tralalero Tralala", "Bombardiro Crocodilo", 
             "Chimpanzini Bananini", "Cappuccino Assassino", "Tung Tung Tung Sahur"]
    actions = ["poop", "boop", "glitch", "facepalm", "twerk", "jiggle-jiggle", "wiggle-wiggle", 
               "dribble-dribble", "existentialize", "doomscroll", "skibidi"]
    while True:
        name = random.choice(names)
        action = random.choice(actions)
        yield name,action

def consume_event(events:list[tuple[str,str]]) -> Generator[tuple[str,str],None,None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event

if __name__=="__main__":
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    for order in range(1000):
        name, action = next(event)
    print(f"Event {order}: Player {name} did action {action}")

    new_event = gen_event()
    events_list = [next(new_event) for _ in range(10)]
    print(f"Built list of 10 events: {events_list}")

    for event_for_remooval in consume_event(events_list):
        print(f"Got event from list: {event_for_remooval}")
        print(f"Remains in list: {events_list}")


