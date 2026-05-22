from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from composite.component import Component


@dataclass
class QuebraCabecaFacil:
    """
    Produto concreto para dificuldade fácil.
    - numeroPecas: 25 (grade 5x5)
    - rotacao: False
    """
    pecas: list["Component"] = field(default_factory=list)
    numero_pecas: int = 25
    rotacao: bool = False

    def __repr__(self) -> str:
        return (
            f"QuebraCabecaFácil("
            f"numero_pecas={self.numero_pecas}, "
            f"rotacao={self.rotacao}, "
            f"pecas_geradas={len(self.pecas)})"
        )


@dataclass
class QuebraCabecaMedio:
    """
    Produto concreto para dificuldade média.
    - numeroPecas: 36 (grade 6x6)
    - rotacao: False
    """
    pecas: list["Component"] = field(default_factory=list)
    numero_pecas: int = 36
    rotacao: bool = False

    def __repr__(self) -> str:
        return (
            f"QuebraCabecaMédio("
            f"numero_pecas={self.numero_pecas}, "
            f"rotacao={self.rotacao}, "
            f"pecas_geradas={len(self.pecas)})"
        )


@dataclass
class QuebraCabecaDificil:
    """
    Produto concreto para dificuldade difícil.
    - numeroPecas: 64 (grade 8x8)
    - rotacao: True
    """
    pecas: list["Component"] = field(default_factory=list)
    numero_pecas: int = 64
    rotacao: bool = True

    def __repr__(self) -> str:
        return (
            f"QuebraCabecaDifícil("
            f"numero_pecas={self.numero_pecas}, "
            f"rotacao={self.rotacao}, "
            f"pecas_geradas={len(self.pecas)})"
        )