from __future__ import annotations

from typing import Literal

from typing_extensions import TypedDict


class KernelDict(TypedDict):
    LTRUNCATE: bool
    IDIMENSIONALITY: Literal[0, 2, 3]
    ISOSURFACE: Literal[1, 2, 3]
    IPAD: int
    FACTOR: float
    LCOARSEN: bool


class VaspIncar(TypedDict, total=False):
    ADDGRID: bool
    AEXX: float
    AGGAC: float
    AGGAX: float
    ALDAC: float
    ALDAX: float
    ALGO: Literal[
        "Normal",
        "VeryFast",
        "Fast",
        "Conjugate ",
        "All",
        "Damped",
        "Subrot ",
        "Eigenval",
        " Exact",
        "None",
        "Nothing",
        " CHI ",
        "G0W0 ",
        "GW0",
        "GW",
        "scGW0",
        "scGW ",
        "G0W0R",
        "GW0R",
        "GWR",
        "scGW0R",
        "scGWR ",
        "ACFDT ",
        "RPA ",
        " ACFDTR ",
        " RPAR",
        "BSE",
        "TDHF",
    ]
    ALPHA_VDW: float
    AMGGAC: float
    AMGGAX: float
    AMIN: float
    AMIX: float
    AMIX_MAG: float
    ANDERSEN_PROB: float
    ANTIRES: Literal[0, 1, 2]
    APACO: float
    BANDGAP: Literal["COMPACT", "WEIGHT", "KPOINT"]
    BEXT: float | list[float]
    BMIX: float
    BMIX_MAG: float
    BPARAM: float
    BSEELECTRON: list[float]
    BSEHOLE: list[float]
    BSEPREC: Literal["Low", "Medium", "High", "Accurate"]
    CH_AMPLIFICATION: float
    CH_LSPEC: bool
    CH_NEDOS: int
    CH_SIGMA: float
    CLL: int
    CLN: int
    CLNT: int
    CLZ: float
    CMBJ: float | list[float]
    CMBJA: float
    CMBJB: float
    CMBJE: float
    CPARAM: float
    CSHIFT: float
    CUTOFF_MU: float | list[float]
    CUTOFF_SIGMA: float | list[float]
    CUTOFF_TYPE: Literal["erfc", "gaussian", "fermi", "num_wann"]
    DEPER: float
    DIMER_DIST: float
    DIPOL: list[float]
    DQ: float
    EBREAK: float
    EDIFF: float
    EDIFFG: float
    EFERMI: Literal["MIDGAP", "LEGACY"] | float
    EFERMI_NEDOS: int
    EFIELD: float
    EFIELD_PEAD: list[float]
    EFOR: list[float]
    EINT: float | list[float]
    ELPH_DECOMPOSE: str
    ELPH_DRIVER: Literal["el", "mels"]
    ELPH_FERMI_NEDOS: int
    ELPH_IGNORE_IMAG_PHONONS: bool
    ELPH_ISMEAR: int
    ELPH_KSPACING: float
    ELPH_LR: int
    ELPH_MODE: str
    ELPH_NBANDS: int
    ELPH_NBANDS_SUM: list[int]
    ELPH_POT_FFT_MESH: list[float]
    ELPH_POT_GENERATE: bool
    ELPH_POT_LATTICE: list[float]
    ELPH_PREPARE: bool
    ELPH_RUN: bool
    ELPH_SCATTERING_APPROX: Literal[
        "CRTA,SERTA", "MRTA_LAMBDA", "ERTA_TAU", "MRTA_LAMDBA", "MRTA_TAU"
    ]
    ELPH_SELFEN_BAND_START: float
    ELPH_SELFEN_BAND_STOP: float
    ELPH_SELFEN_BROAD_TOL: float
    ELPH_SELFEN_CARRIER_DEN: list[float]
    ELPH_SELFEN_CARRIER_DEN_RANGE: list[float]
    ELPH_SELFEN_CARRIER_PER_CELL: list[float]
    ELPH_SELFEN_DELTA: list[float]
    ELPH_SELFEN_DW: bool
    ELPH_SELFEN_ENERGY_WINDOW: list[float]
    ELPH_SELFEN_FAN: bool
    ELPH_SELFEN_G_SKIP: bool
    ELPH_SELFEN_GAPS: bool
    ELPH_SELFEN_IKPT: list[float]
    ELPH_SELFEN_IMAG_SKIP: bool
    ELPH_SELFEN_KPTS: list[float]
    ELPH_SELFEN_MU: list[float]
    ELPH_SELFEN_MU_RANGE: list[float]
    ELPH_SELFEN_NW: int
    ELPH_SELFEN_STATIC: bool
    ELPH_SELFEN_TEMPS: list[float]
    ELPH_SELFEN_TEMPS_RANGE: list[float]
    ELPH_SELFEN_WRANGE: float
    ELPH_TRANSPORT: bool
    ELPH_TRANSPORT_DFERMI_TOL: float
    ELPH_TRANSPORT_DRIVER: int
    ELPH_TRANSPORT_EMAX: float
    ELPH_TRANSPORT_EMAX_PLOT: float
    ELPH_TRANSPORT_EMIN: float
    ELPH_TRANSPORT_EMIN_PLOT: float
    ELPH_TRANSPORT_NEDOS_PLOT: int
    ELPH_USEBLAS: bool
    ELPH_WF_CACHE_PREFILL: bool
    ELPH_WF_COMM_OPT: Literal[0, 1]
    ELPH_WF_REDISTRIBUTE: bool
    ELPH_WRITE_HDF5VEL: bool
    ELPH_WRITE_TEXTVEL: bool
    EMAX: float
    EMIN: float
    ENAUG: float
    ENCUT: tuple
    ENCUTFOCK: float
    ENCUTGW: float
    ENCUTGWSOFT: float
    ENCUTLR: float
    ENINI: float
    EPSILON: float
    ESTOP: float
    EVENONLY: bool
    EVENONLYGW: bool
    FBIAS_A: float | list[float]
    FBIAS_D: float | list[float]
    FBIAS_R0: float | list[float]
    FERDO: list[float]
    FERWE: list[float]
    FINDIFF: int
    FMP_ACTIVE: list[bool]
    FMP_DIRECTION: Literal[1, 2, 3]
    FMP_PERIOD: int
    FMP_SNUMBER: int
    FMP_SWAPNUM: int
    FOCKCORR: Literal[1, 2]
    GAMMA_VDW: float
    GGA: str
    GGA_COMPAT: bool
    HFALPHA: float
    HFLMAX: int
    HFRCUT: float
    HFSCREEN: float
    HILLS_BIN: int
    HILLS_H: float
    HILLS_W: float
    HITOLER: float
    I_CONSTRAINED_M: Literal[1, 2, 4] | None
    IALGO: Literal[
        -1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        15,
        16,
        17,
        18,
        28,
        38,
        44,
        45,
        46,
        47,
        48,
        53,
        54,
        55,
        56,
        57,
        58,
    ]
    IALL_IN_ONE: Literal[1, -1]
    IBAND: list[int]
    IBRION: Literal[-1, 0, 1, 2, 3, 5, 6, 7, 8, 11, 12, 40, 44]
    IBSE: Literal[0, 1, 2, 3]
    ICHARG: Literal[0, 1, 2, 4, 5, 10, 11, 12]
    ICHIBARE: Literal[1, 2, 3]
    ICORELEVEL: Literal[0, 1, 2]
    IDIPOL: Literal[1, 2, 3, 4]
    IEPSILON: Literal[1, 2, 3, 4]
    IFC_ASR: int
    IFC_LR: int
    IGPAR: Literal[1, 2, 3]
    IMAGES: int
    IMIX: Literal[0, 1, 2, 4]
    INCREM: list[float]
    INIMIX: Literal[0, 1, 2]
    INIWAV: Literal[0, 1]
    IPEAD: Literal[1, 2, 3, 4]
    IRC_DELTA0: float
    IRC_DIRECTION: Literal[-1, 1]
    IRC_MAXSTEP: float
    IRC_MINSTEP: float
    IRC_STOP: int
    IRC_VNORM0: float
    ISEARCH: Literal[0, 1]
    ISIF: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8]
    ISMEAR: int
    ISPIN: Literal[1, 2]
    ISTART: Literal[0, 1, 2, 3]
    ISYM: Literal[-1, 0, 1, 2, 3]
    IVDW: Literal[1, 2, 3, 4, 10, 11, 12, 13, 14, 20, 21, 202, 263]
    IVDW_NL: Literal[1, 2]
    IWAVPR: Literal[0, 1, 2, 3, 10, 11, 12, 13]
    KBLOCK: int
    KERNEL_TRUNCATION_FACTOR: KernelDict
    KGAMMA: bool
    KPAR: int
    KPOINT_BSE: int | list[int]
    KPOINTS_OPT_MODE: Literal[0, 1, 2]
    KPOINTS_OPT_NKBATCH: int
    KPUSE: list[int]
    KSPACING: float
    LADDER: bool
    LAECHG: bool
    LALL_IN_ONE: bool
    LAMBDA: float
    LANCZOSTHR: float
    LANGEVIN_GAMMA: list[float]
    LANGEVIN_GAMMA_L: float
    LASPH: bool
    LASYNC: bool
    LATTICE_CONSTRAINTS: list[bool]
    LBERRY: bool
    LBLUEOUT: bool
    LBONE: bool
    LCALCEPS: bool
    LCALCPOL: bool
    LCHARG: bool
    LCHARGH5: bool
    LCHIMAG: bool
    LCORR: bool
    LDAU: bool
    LDAUJ: list[float]
    LDAUL: list[int]
    LDAUPRINT: Literal[0, 1]
    LDAUTYPE: Literal[1, 2, 3, 4]
    LDAUU: list[float]
    LDIAG: bool
    LDIPOL: bool
    LDISENTANGLED: bool
    LDMATRIX: bool
    LDOWNSAMPLE: bool
    LEFG: bool
    LELF: bool
    LEPSILON: bool
    LFINITE_TEMPERATURE: bool
    LFOCKACE: bool
    LFOCKAEDFT: bool
    LFOCKSTD: bool
    LFXC: bool
    LH5: bool
    LHARTREE: bool
    LHFCALC: bool
    LHYPERFINE: bool
    LIBMBD_ALPHA: list[float]
    LIBMBD_C6AU: list[float]
    LIBMBD_K_GRID: list[int]
    LIBMBD_K_GRID_SHIFT: float
    LIBMBD_MBD_A: float
    LIBMBD_MBD_BETA: float
    LIBMBD_METHOD: str
    LIBMBD_N_OMEGA_GRID: int
    LIBMBD_PARALLEL_MODE: Literal["auto", "kpoints,atoms"]
    LIBMBD_R0AU: list[float]
    LIBMBD_TS_D: float
    LIBMBD_TS_SR: float
    LIBMBD_VDW_PARAMS_KIND: Literal["ts", "tssurf"]
    LIBMBD_XC: Literal["pbe", "pbe0", "hse", "blyp", "b3lyp", "revpbe", "am05", "none"]
    LIBXC1: str | int
    LIBXC1_Pn: float
    LIBXC2: str | int
    LIBXC2_Pn: float
    LKPOINTS_OPT: bool
    LKPOINTS_WAN: bool
    LKPROJ: bool
    LLRAUG: bool
    LMAXFOCK: int
    LMAXFOCKAE: int
    LMAXMIX: int
    LMAXPAW: int
    LMAXTAU: int
    LMIXTAU: bool
    LMODELHF: bool
    LMONO: bool
    LMP2LT: bool
    LNABLA: bool
    LNICSALL: bool
    LNMR_SYM_RED: bool
    LNOAUGXC: bool
    LNONCOLLINEAR: bool
    LOCPROJ: str | list[str]
    LOPTICS: bool
    LORBIT: Literal[0, 1, 2, 5, 10, 11, 12, 13, 14]
    LORBMOM: bool
    LPARD: bool
    LPARDH5: bool
    LPEAD: bool
    LPHON_DISPERSION: bool
    LPHON_POLAR: bool
    LPHON_READ_FORCE_CONSTANTS: bool
    LPLANE: bool
    LPOSNICS: bool
    LREAL: Literal["Auto", "On"] | bool
    LRHFCALC: bool
    LRPA: bool
    LRPAFORCE: bool
    LSCAAWARE: bool
    LSCALAPACK: bool
    LSCALER0: bool
    LSCALU: bool
    LSCDM: bool
    LSCK: bool
    LSCRPA: bool
    LSCSGRAD: bool
    LSELFENERGY: bool
    LSEPB: bool
    LSEPK: bool
    LSFBXC: bool
    LSINGLES: bool
    LSMP2LT: bool
    LSORBIT: bool
    LSPECTRAL: bool
    LSPECTRALGW: bool
    LSPIN_VDW: bool
    LSPIRAL: bool
    LSUBROT: bool
    LSYNCH5: bool
    LTBOUNDLIBXC: bool
    LTEMPER: bool
    LTHOMAS: bool
    LTRIPLET: bool
    LTSSURF: bool
    LUSE_VDW: bool
    LUSENCCL: bool
    LVACPOTAV: bool
    LVDW_EWALD: bool
    LVDW_ONECELL: list[bool]
    LVDWEXPANSION: bool
    LVDWSCS: bool
    LVGVAPPL: bool
    LVGVCALC: bool
    LVHAR: bool
    LVTOT: bool
    LWANNIER90: bool
    LWANNIER90_RUN: bool
    LWAVE: bool
    LWAVEH5: bool
    LWEIGHTED: bool
    LWRITE_MMN_AMN: bool
    LWRITE_SPN: bool
    LWRITE_UNK: bool
    LWRITE_WANPROJ: bool
    LZEROZ: bool
    M_CONSTR: list[float]
    MAGMOM: list[float]
    MAXMEM: int
    MAXMIX: int
    MDALGO: Literal[0, 1, 2, 3, 4, 5, 11, 21, 13]
    METAGGA: str
    MINROT: float
    MIXPRE: Literal[0, 1, 2, 3]
    ML_AFILT2: float
    ML_CALGO: Literal[0, 1]
    ML_CDOUB: float
    ML_CSIG: float
    ML_CSLOPE: float
    ML_CX: float
    ML_DESC_TYPE: Literal[0, 1]
    ML_EATOM_REF: list[float]
    ML_EPS_LOW: float
    ML_EPS_REG: float
    ML_ESTBLOCK: int
    ML_IAFILT2: int
    ML_IALGO_LINREG: Literal[1, 2, 3, 4]
    ML_ICOUPLE: list[int]
    ML_ICRITERIA: Literal[0, 1, 2, 3]
    ML_IREG: Literal[1, 2]
    ML_ISCALE_TOTEN: Literal[1, 2]
    ML_ISTART: Literal[0, 1, 2, 3, 4]
    ML_IWEIGHT: Literal[1, 2, 3]
    ML_LAFILT2: bool
    ML_LBASIS_DISCARD: bool
    ML_LCOUPLE: bool
    ML_LEATOM: bool
    ML_LERR: bool
    ML_LFAST: bool
    ML_LHEAT: bool
    ML_LIB: bool
    ML_LMAX2: int
    ML_LMLFF: bool
    ML_LSPARSDES: bool
    ML_LUSE_NAMES: bool
    ML_MB: int
    ML_MB_MIN: int
    ML_MCONF: int
    ML_MCONF_NEW: int
    ML_MHIS: int
    ML_MODE: Literal["train", "select", "refit", "refitbayesian", "run", "none"]
    ML_MRB1: int
    ML_MRB2: int
    ML_NATOM_COUPLED: int
    ML_NHYP: int
    ML_NMDINT: int
    ML_NRANK_SPARSDES: int
    ML_OUTBLOCK: int
    ML_OUTPUT_MODE: Literal[0, 1]
    ML_RCOUPLE: float
    ML_RCUT1: float
    ML_RCUT2: float
    ML_RDES_SPARSDES: float
    ML_SCLC_CTIFOR: float
    ML_SIGV0: float
    ML_SIGW0: float
    ML_SION1: float
    ML_SION2: float
    ML_W1: float
    ML_WTIFOR: float
    ML_WTOTEN: float
    ML_WTSIF: float
    NATURALO: int
    NBANDS: int
    NBANDS_WAVE: int
    NBANDSEXACT: int
    NBANDSGW: int
    NBANDSO: int
    NBANDSV: int
    NBLK: int
    NBLOCK: int
    NBMOD: int
    NBSEBLOCKO: int
    NBSEBLOCKV: int
    NBSEEIG: int
    NCORE: int
    NCORE_IN_IMAGE1: int
    NCRPA_BANDS: list[int]
    NEDOS: int
    NELECT: float
    NELM: int
    NELMDL: int
    NELMGW: int
    NELMIN: int
    NFREE: int
    NGX: int
    NGXF: int
    NGY: int
    NGYF: int
    NGYROMAG: list[float]
    NGZ: int
    NGZF: int
    NHC_NCHAINS: int
    NHC_NRESPA: int
    NHC_NS: int
    NKRED: int
    NKREDX: int
    NKREDY: int
    NKREDZ: int
    NLSPLINE: bool
    NMAXFOCKAE: Literal[1, 2]
    NOMEGA: int
    NOMEGA_DUMP: int
    NOMEGAPAR: int
    NOMEGAR: int
    NPACO: int
    NPAR: int
    NPPSTR: int
    NRMM: int
    NSIM: int
    NSTORB: int
    NSUBSYS: list[int]
    NSW: int
    NTARGET_STATES: list[int]
    NTAUPAR: int
    NTEMPER: int
    NUCIND: bool
    NUM_WANN: int
    NUPDOWN: float
    NWRITE: Literal[0, 1, 2, 3, 4]
    ODDONLY: bool
    ODDONLYGW: bool
    OFIELD_A: float
    OFIELD_KAPPA: float
    OFIELD_Q6_FAR: float
    OFIELD_Q6_NEAR: float
    OMEGAMAX: float
    OMEGAMIN: float
    OMEGATL: float
    PARAM1: float
    PARAM2: float
    PFLAT: bool
    PHON_BORN_CHARGES: list[float]
    PHON_DIELECTRIC: list[float]
    PHON_DOS: Literal[0, 1, 2]
    PHON_G_CUTOFF: float
    PHON_LBOSE: bool
    PHON_LMC: bool
    PHON_NEDOS: int
    PHON_NSTRUCT: int
    PHON_NTlist: int
    PHON_NWRITE: Literal[2, 1, 0, -1, -2, -3]
    PHON_SIGMA: float
    PHON_Tlist: list[float]
    PLEVEL: int
    PLUGINS_FORCE_AND_STRESS: bool
    PLUGINS_LOCAL_POTENTIAL: bool
    PLUGINS_MACHINE_LEARNING: bool
    PLUGINS_OCCUPANCIES: bool
    PLUGINS_STRUCTURE: bool
    PMASS: float
    POMASS: list[float]
    POTIM: float
    PREC: Literal["Normal", "Single", "SingleN", "Accurate", "Low", "Medium", "High"]
    PRECFOCK: Literal["Normal", "Accurate", "Fast", "Medium", "Single"]
    # Profiling:
    PROUTINE: int
    PSTRESS: float
    PSUBSYS: list[float]
    PTHRESHOLD: float
    QMAXFOCKAE: list[float]
    QSPIRAL: list[float]
    QUAD_EFG: list[float]
    RANDOM_GENERATOR: Literal["default", "pcg_32"]
    RANDOM_SEED: list[int]
    ROPT: list[float]
    RSMBJ: float
    RWIGS: list[float]
    SAXIS: list[float]
    SCALEE: float
    SCISSOR: float
    SCSRAD: float
    SHAKEMAXITER: int
    SHAKETOL: float
    SIGMA: float
    SMASS: Literal[-3, -2, -1] | float
    SMBJ: float
    SMEARINGS: list[float]
    SPRING: int
    SPRING_K: float | list[float]
    SPRING_R0: float | list[float]
    SPRING_V0: float | list[float]
    STEP_MAX: float
    STEP_SIZE: float
    STOP_ON: Literal["Error", "Alert"]
    SYMPREC: float
    SYSTEM: str
    TEBEG: float
    TEEND: float
    TILAMBDA: float
    TIME: float
    TRANSPORT_NEDOS: int
    TRANSPORT_RELAXATION_TIME: float
    TSUBSYS: list[float]
    VACPOTFLAT: float
    VALUE_MAX: list[float]
    VALUE_MIN: list[float]
    VCA: list[float]
    VCAIMAGES: float
    VCUTOFF: float
    VDW_A1: float
    VDW_A2: float
    VDW_ALPHA: float | list[float]
    VDW_C6: float | list[float]
    VDW_C6AU: float | list[float]
    VDW_CNRADIUS: float
    VDW_D: float
    VDW_R0: float | list[float]
    VDW_R0AU: float | list[float]
    VDW_RADIUS: float
    VDW_S6: float
    VDW_S8: float
    VDW_SR: float
    VELOCITY: bool
    VOSKOWN: Literal[0, 1]
    WANNIER90_WIN: str
    WC: float
    WEIMIN: float
    WRT_NMRCUR: Literal[0, 1, 2, 3, 4]
    WRT_POTENTIAL: str
    XC: str
    XC_C: list[float]
    ZAB_VDW: float
