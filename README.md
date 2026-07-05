Sila RLP
============

Recursive-length prefix (RLP) serialization as used by the [Sila Execution Layer Specification (EELS)][eels].

[eels]: https://github.com/sila-chain/execution-specs

## Usage

Here's a very basic example demonstrating how to define a schema, then encode/decode it:

```python
from dataclasses import dataclass
from sila_rlp import encode, decode_to
from sila_types.numeric import Uint
from typing import List

@dataclass
class Stuff:
    toggle: bool
    number: Uint
    sequence: List["Stuff"]

encoded = encode(Stuff(toggle=True, number=Uint(3), sequence=[]))
decoded = decode_to(Stuff, encoded)
assert decoded.number == Uint(3)
```

See the `tests/` directory for more examples.
