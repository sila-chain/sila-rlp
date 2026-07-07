"""
Defines the serialization and deserialization format used throughout Sila.
"""

from .sila_rlp import (  # noqa: F401
    SILA_RLP,
    Extended,
    Simple,
    With,
    decode,
    decode_to,
    encode,
)

__version__ = "0.1.7"
