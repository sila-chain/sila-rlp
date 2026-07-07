"""
Exceptions that can be thrown while serializing/deserializing SILA_RLP.
"""

from typing_extensions import override


class SILA_RLPException(Exception):
    """
    Common base class for all SILA_RLP exceptions.
    """


class DecodingError(SILA_RLPException):
    """
    Indicates that SILA_RLP decoding failed.
    """

    @override
    def __str__(self) -> str:
        message = [super().__str__()]
        current: BaseException = self
        while isinstance(current, DecodingError) and current.__cause__:
            current = current.__cause__
            if isinstance(current, DecodingError):
                as_str = super(DecodingError, current).__str__()
            else:
                as_str = str(current)
            message.append(f"\tbecause {as_str}")
        return "\n".join(message)


class EncodingError(SILA_RLPException):
    """
    Indicates that SILA_RLP encoding failed.
    """
