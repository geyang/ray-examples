import ray


@ray.remote
class Actor:
    def say_hello(self, message):
        print(message)


# driver_1.py
# Job 1 creates an actor, "orange" in the "colors" namespace.
ray.init(address="auto", namespace="colors")
Actor.options(name="orange", lifetime="detached").remote()

# Actor `yellow` doesn't yet exist, so it is created with the given args.
a = Color.options(name="yellow", get_if_exists=True).remote("I'm Yellow")
assert ray.get(a.say_hello.remote()) == "I'm Yellow"

# Actor `green` already exists, so it is returned (new args are ignored).
b = Greeter.options(name="yellow", get_if_exists=True).remote("I'm Green")
assert ray.get(b.say_hello.remote()) == "Old Greeting"
