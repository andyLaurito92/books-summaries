## Implementation-defined behaviour

The C standard leaves parts of the language unspecified, w/the understanding that an "implementation" (compiler, linker, executable on 
a particular platform) will fill in the details

Because of the above, behaviour of the programs may vary according to the platform it's bein executed --> Not that portable :)

## L-values

An object stored in memory, example: A variable

## A bit of history

++ & -- operators come from the B language :). Apparently in the B language, the compiler could generate a more compact translation for
++i than i = i + 1k
