"""
SMILES
======

"""

from __future__ import annotations

from ..molecules import Molecule
from .molecule import MoleculeKeyMaker
from .utilities import get_smiles


class Smiles(MoleculeKeyMaker):
    """
    Used to get the SMILES of molecules.

    Examples:

        *Adding SMILES to a Molecule's JSON*

        You want to use the isomeric, canonical SMILES from RDKit as
        part of a JSON representation of a molecule

        .. testcode:: adding-smiles-to-a-molecules-json

            import stk

            jsonizer = stk.MoleculeJsonizer(
                key_makers=(stk.Smiles(), ),
            )
            # Get the JSON representation, including an SMILES.
            json = jsonizer.to_json(stk.BuildingBlock('NCCN'))

        .. testcode:: adding-smiles-to-a-molecules-json
            :hide:

            assert json['molecule']['SMILES'] == 'NCCN'
            assert json['matrix']['SMILES'] == 'NCCN'

    """

    def __init__(self) -> None:
        """
        Initialize a :class:`.Smiles` instance.

        """

        pass

    def get_key_name(self) -> str:
        return "SMILES"

    def get_key(self, molecule: Molecule) -> str:
        return get_smiles(molecule)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return "Smiles()"
