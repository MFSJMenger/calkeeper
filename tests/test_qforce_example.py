"""Basic tests for calculations using qforce_examples"""
from pathlib import Path
#
import pytest
from qforce_examples import Gaussian_default, Orca_default
from calkeeper import CalculationKeeper, CalculationIncompleteError


@pytest.fixture
def keeper():
    """Return basic CalculationKeeper instance"""
    return CalculationKeeper()


@pytest.fixture
def gaudefault_files():
    """Gaussian files in Gaussian_default"""
    return {'out_file': ['necessary_files/${base}_hessian.out'],
            'chk_file': ['necessary_files/${base}_hessian.fchk'],
            'fragments': [
                'necessary_files/fragments/CC_H8C3_d91b46644317dee9c2b868166c66a18c~1.out'],
            'xyz_file': ['${base}.xyz'],
            }


@pytest.fixture
def orcadefault_files():
    """Orca files in Orca_default"""
    return {'pc_chelpg': ['necessary_files/${base}_charge.pc_chelpg'],
            'out_file':  ['necessary_files/${base}_hessian.out'],
            'hess': ['necessary_files/${base}_opt.hess'],
            'opt': ['necessary_files/${base}_opt.xyz'],
            }


def test_gaufiles(keeper, gaudefault_files):
    """Test basic files in Gaussian_default"""
    inp = Path(Gaussian_default['xyz_file'])
    folder = inp.parent
    cal = keeper.calculation(inp.name, gaudefault_files, folder=folder)

    try:
        cal.check()
        assert True
    except CalculationIncompleteError as err:
        assert False, str(err)


def test_orcafiles(keeper, orcadefault_files):
    """Test basic files in Orca_default"""
    inp = Path(Orca_default['xyz_file'])
    folder = inp.parent
    cal = keeper.calculation(inp.name, orcadefault_files, folder=folder)

    try:
        cal.check()
        assert True
    except CalculationIncompleteError as err:
        assert False, str(err)
