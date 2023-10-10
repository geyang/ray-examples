# Ray Examples

I used this repo to learn how to write Async code with Pyro5, and then ray.

Pyro5's maintainer has made some bizzar decisions, and the project is practically dead. So after I wrote a version of our new project using Pyro4 (after migrating from Pyro5...), I decided to rewrite it using ray. The key resons for this rewrite are:

 1. Pyro5 does not support pickle or cloudpickle serialization ([this guy is a douche](https://github.com/irmen/Pyro5/issues/16)).
 2. Pyro4 does support those, but it does not support async function on the client side.
 3. Ray supports both.

 At last I needed to figure out how to setup a persistent Ray worker, so that I can fire up the LLM inference server and keep it running.
  This is called a named actor in Ray.

 See the code for details.

 Ge
