from __future__ import annotations

from alchemio.vasp.incar import read_incar,write_incar
from alchemio.vasp.vasp_types import VaspIncar, KernelDict
from alchemio.vasp.utils import format_value,clean_value,parse_number

def test_read_incar() -> None:
    """Test the read_incar function from the vasp module."""
    
    incar = read_incar("test_files/INCAR")

    assert incar.get("ISTART") == 1
    assert incar.get("LREAL") == False
    assert incar.get("PREC")== "Accurate"
    assert incar.get("SIGMA") == 0.05
    assert incar.get("EDIFF") == 1E-04
    assert incar.get("ENCUT") == (300.0, 'eV')
    assert incar.get("WANNIER90_WIN") == '"\n  Begin Projections\n  Si:sp3\n  End Projections\n  "'

    assert incar.get("MAGMOM") == [0, 0, 1.0, 0, 0, -1.0, 0, 0, 1.0, 0, 0, -1.0, 0, 0, 0, 0, 0, 0]
    assert incar.get("KERNEL_TRUNCATION") == {
    "LTRUNCATE"       : True,
    "IDIMENSIONALITY" : 2,
    "ISURFACE"        : 3,
    "IPAD"            : 1,
    "FACTOR"          : 0.5
}


def test_write_incar() -> None:
    """Test the write_incar function from the vasp module."""
    
    incar_dict = {
        "ISTART" : 1,
        "LREAL": False,
        "PREC": "Accurate",
        "SIGMA": 0.05,
        "EDIFF": 1E-04,
        "ENCUT": (300.0, 'eV'),
        "MAGMOM" :[0, 0, 1.0, 0, 0, -1.0, 0, 0, 1.0, 0, 0, -1.0, 0, 0, 0, 0, 0, 0],
        "KERNEL_TRUNCATION" : 
        {
          "LTRUNCATE"       : True,
          "IDIMENSIONALITY" : 2,
          "ISURFACE"        : 3,
          "IPAD"            : 1,
          "FACTOR"          : 0.5
        },
        "WANNIER90_WIN" : '"\n  Begin Projections\n  Si:sp3\n  End Projections\n  "'

    }
    incar = VaspIncar(**incar_dict)
    
    write_incar(incar,"test_files/incar_test.txt")

    with open("test_files/incar_test.txt") as f:
        lines = f.readlines()
      
    lines=[line.strip() for line in lines]
    
    assert lines[0] == 'ISTART = 1'
    assert lines[1] == 'LREAL = .FALSE.'
    assert lines[2] == 'PREC = Accurate'
    assert lines[3] == 'SIGMA = 0.05'
    assert lines[4] == 'EDIFF = 0.0001'
    assert lines[5] == 'ENCUT = 300.0 eV'
    assert lines[6] == 'MAGMOM = 0 0 1.0 0 0 -1.0 0 0 1.0 0 0 -1.0 0 0 0 0 0 0'
    assert lines[7] == 'KERNEL_TRUNCATION {'
    assert lines[8] == 'LTRUNCATE = .TRUE.'
    assert lines[9] == 'IDIMENSIONALITY = 2'
    assert lines[10] == 'ISURFACE = 3'
    assert lines[11] == 'IPAD = 1'
    assert lines[12] == 'FACTOR = 0.5'
    assert lines[13] == '}'

    assert lines[14]==  "WANNIER90_WIN = \"\""
    assert lines[15]==  "Begin Projections"
    assert lines[16]==  "Si:sp3"
    assert lines[17]==  "End Projections"
    assert lines[18]==  "\"\""

    

def test_vaspincar() -> None:
  
  incar_dict = {
    "ISTART" : 1,
    "LREAL": False,
    "PREC": "Accurate",
    "SIGMA": 0.05,
    "ENCUT": (300.0, 'eV'),
    "MAGMOM" :[0, 0, 1.0, 0, 0, -1.0, 0, 0, 1.0, 0, 0, -1.0, 0, 0, 0, 0, 0, 0],
    "KERNEL_TRUNCATION" : 
    {
      "LTRUNCATE"       : True,
      "IDIMENSIONALITY" : 2,
      "ISURFACE"        : 3,
      "IPAD"            : 1,
      "FACTOR"          : 0.5
    },

  }
  
  incar = VaspIncar(**incar_dict)

  assert incar.get("ISTART") == 1
  assert incar.get("LREAL") == False
  assert incar.get("PREC") == "Accurate"
  assert incar.get("SIGMA") == 0.05
  assert incar.get("ENCUT") == (300.0, 'eV')
  assert incar.get("MAGMOM") == [0, 0, 1.0, 0, 0, -1.0, 0, 0, 1.0, 0, 0, -1.0, 0, 0, 0, 0, 0, 0]
  assert incar.get("KERNEL_TRUNCATION") == {
      "LTRUNCATE"       : True,
      "IDIMENSIONALITY" : 2,
      "ISURFACE"        : 3,
      "IPAD"            : 1,
      "FACTOR"          : 0.5
    }



def test_clean_value()-> None:
    
    assert clean_value(".TRUE.") is True
    assert clean_value("TRUE") is True
    assert clean_value("F") is False

    assert clean_value("42 # comment") == 42
    assert clean_value("3.14 ! comment") == 3.14
    assert clean_value("100 (note)") == 100

    assert clean_value("-7") == -7
    assert clean_value("+100") == 100

    assert clean_value("1e-9") == 1e-9
    assert clean_value("1.2E+3") == 1200.0

    assert clean_value("300 eV") == (300, "eV")
    assert clean_value("100MHz") == (100.0, "MHz")

    assert clean_value("4*-1") == [-1, -1, -1, -1]
    assert clean_value("2*0 1") == [0, 0, 1]

def test_format_value()-> None:
    LREAL= False
    MAGMOM =[0, 0, 1.0, 0, 0, -1.0, 0, 0, 1.0, 0, 0, -1.0, 0, 0, 0, 0, 0, 0]

    assert format_value(LREAL) == ".FALSE."
    assert format_value(MAGMOM) == "0 0 1.0 0 0 -1.0 0 0 1.0 0 0 -1.0 0 0 0 0 0 0"

def test_parse_number() -> None:
    

    assert parse_number(4) == 4
    assert parse_number(4.3) == 4.3
    assert parse_number("300 eV") == (300, "eV")
    assert parse_number("5") == 5
    assert parse_number(True) == True
    assert parse_number(3.14e10) == 3.14e10
    assert parse_number(-3.14e10) == -3.14e10
    assert parse_number("+5") == 5
    assert parse_number("-10") == -10
    assert parse_number(-4) == -4
