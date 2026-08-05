import subprocess
from enum import Enum
from dataclasses import dataclass

from pyosys import libyosys as ys

#PRIMITIVES = "~/VLSI/PDK/test-pdk/sky130A/libs.ref/sky130_fd_sc_hd/verilog/primitives.v"
PRIMITIVES = "primitives.v"
FUNCTIONAL = "~/VLSI/PDK/test-pdk/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v"
#FUNCTIONAL = "sky130_fd_sc_hd.v"
LIBERTY    = "~/VLSI/PDK/test-pdk/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib"
DONTUSE = "-dont_use *clkinv* -dont_use *lpflow*"

class Timing(Enum):
   SLOW = 0
   MEDIUM = 1
   FAST = 2

@dataclass
class DutUnit:
    name: str
    timing: list

sources = [f"../src/{unit}.sv" for unit in [
    "arith_utils",
    "AbsVal",
    "Add",
    "AddC",
    "AddCfast",
    "AddCsv",
    "AddMod2Nm1",
    "AddMod2Nm1s0",
    "AddMod2Np1",
    "AddMop",
    "AddMopCsv",
    "AddMulPPGenSgn",
    "AddMulPPGenUns",
    "AddMulSgn",
    "AddMulUns",
    "AddSub",
    "AddSubC",
    "AddSubV",
    "AddV",
    "AllOneDet",
    "AllZeroDet",
    "Bin2Gray",
    "CmpEQ",
    "CmpEQGE",
    "CmpGE",
    "Cnt",
    "CntSlice",
    "Cpr",
    "Dec",
    "DecC",
    "Decode",
    "DivArrSgn",
    "DivArrUns",
    "Encode",
    "FullAdder",
    "Gray2Bin",
    "Inc",
    "IncC",
    "IncDec",
    "IncDecC",
    "IncGray",
    "IncGrayC",
    "LeadOneDet",
    "LeadSignDet",
    "LeadZeroDet",
    "Log2",
    "MulAddSgn",
    "MulAddUns",
    "MulCsvSgn",
    "MulCsvUns",
    "MulPPGenSgn",
    "MulPPGenUns",
    "MulSgn",
    "MulUns",
    "Neg",
    "NegC",
    "PrefixAnd",
    "PrefixAndOr",
    "PrefixAndOrCendaround",
    "PrefixAndOrCfast",
    "PrefixOr",
    "PrefixXor",
    "RedAnd",
    "RedOr",
    "RedXor",
    "Reg",
    "SqrPPGenSgn",
    "SqrPPGenUns",
    "SqrSgn",
    "SqrUns",
    "SqrtArrUns",
    "Sub",
    "SubC",
    "SubCZ",
    "SubV",
    "SubVZ",
    "SumZeroDet",
]]


def unit_test(dut: DutUnit):

    for timing in dut.timing:

        stepidx = 0
        def report (name: str):
            global stepidx
            stepname = f"reports/{dut.name}_{stepidx}_{name}"
            ys.run_pass(f"dump")
            ys.run_pass(f"stat")
            ys.run_pass(f"write_verilog {stepname}.v")
            ys.run_pass(f"write_json {stepname}.json")
            subprocess.Popen(f'netlistsvg {stepname}.json -o {stepname}.svg', shell=True)
            stepidx = stepidx + 1

        print(f"#######################################")
        print(f"# DUT: {dut.name}, speed={timing.value}")
        print(f"#######################################")

        # read design
        ys.run_pass(f"read_slang -top {dut.name} --relax-enum-conversions -G speed={timing.value} ../src/arith_utils.sv " + " ".join(sources))

        #######################################
        # RTL
        #######################################

        # process optimized RTL
#        ys.run_pass(f"hierarchy -check -top {dut.name}")
#        ys.run_pass(f"select -list")

        # the high-level stuff
#        ys.run_pass(f"proc; opt")
#        ys.run_pass(f"memory; opt")
#        ys.run_pass(f"fsm; opt")
#        report("proc")

#        ys.run_pass(f"flatten")

        # map simple cells to gate primitives
        ys.run_pass(f"equiv_opt -assert -async2sync simplemap")
        ys.run_pass(f"simplemap; opt")
#        report("simplemap")
#        ys.run_pass(f"show -prefix simplemap {dut.name}")
#        ys.run_pass(f"shell")

        # mapping to internal cell library

#        ys.run_pass(f"alumacc")
#        report("alumacc")
#        ys.run_pass(f"equiv_opt -map {LIBERTY} -map {PRIMITIVES} -map {FUNCTIONAL} -assert techmap -map rca_map.v")
#        ys.run_pass(f"show -prefix alumacc {dut.name}")
#        ys.run_pass(f"shell")

#        ys.run_pass(f"opt_expr")
#        report("alumacc_opt_expr")
#        ys.run_pass(f"equiv_opt -map {LIBERTY} -map {PRIMITIVES} -map {FUNCTIONAL} -assert techmap -map rca_map.v")
#        ys.run_pass(f"show -prefix alumacc_opt_expr {dut.name}")

#        ys.run_pass(f"techmap -map librelane_rca_map.v -map librelane_fa_map.v")
#        ys.run_pass(f"show -prefix techmap_rca_map {dut.name}")
#        ys.run_pass(f"opt")
#        ys.run_pass(f"show -prefix techmap_rca_map_opt {dut.name}")

        # mapping to internal cell library
        ys.run_pass(f"techmap")
#        report("techmap")
#        ys.run_pass(f"show -prefix techmap {dut.name}")
#        ys.run_pass(f"opt")
#        report("techmap_opt")
#        ys.run_pass(f"show -prefix techmap_opt {dut.name}")
#        ys.run_pass(f"shell")

#        ys.run_pass(f"opt_merge;")
#        report("opt_merge")
##        ys.run_pass(f"shell")

#        # mapping logic to SCL
#        ys.run_pass(f"abc -liberty {LIBERTY} {DONTUSE}")
#        report("abc")
#
#        ## write synthesized design
#        ys.run_pass(f"write_verilog {dut.name}_netlist.v")
#        ys.run_pass(f"write_json {dut.name}_netlist.json")
#

        #######################################
        # reference
        #######################################

        # read design
        ys.run_pass(f"read_slang -top behavioural_{dut.name} ../src/arith_utils.sv " + " ".join(sources))
        # process optimized RTL
#        ys.run_pass(f"hierarchy -check -top behavioural_{dut.name}")
#        ys.run_pass(f"select -list")

        # the high-level stuff
#        ys.run_pass(f"proc; opt")
#        ys.run_pass(f"memory; opt")
#        ys.run_pass(f"fsm; opt")
#        report("proc")

        #######################################
        # equivalence check
        #######################################

#        ys.run_pass(f"opt_clean -purge")
        # create a miter circuit to test equivalence
        ys.run_pass(f"miter -equiv -make_assert -make_outputs behavioural_{dut.name} {dut.name} miter")
        ys.run_pass(f"hierarchy -top miter")
        ys.run_pass(f"flatten")
        # run equivalence check
        ys.run_pass(f"sat -verify -prove-asserts -show-inputs -show-outputs -show-public miter")

        # cleanup
#        clean

#        # create SVG schematic
#        subprocess.Popen('netlistsvg {dut.name}_netlist.json -o {dut.name}_netlist.svg', shell=True)

        ys.run_pass(f"design -reset")

units = [
    # Adders
    DutUnit("Add"                  , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("AddC"                 , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("AddCfast"             , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("AddV"                 , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("AddMod2Nm1"           , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("AddMod2Nm1s0"         , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
#   DutUnit("AddMod2Np1"           , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # equivalence fail
    DutUnit("AddCsv"               , [                            Timing.FAST]),
    DutUnit("AddMop"               , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
#    DutUnit("AddMopCsv"            , [Timing.SLOW,                Timing.FAST]), # missing behavioral

    # helper for AddMod2N*
#   DutUnit("PrefixAndOrCendaround", [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral
    # helper for AddCfast
#   DutUnit("PrefixAndOrCfast"     , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral

    # Subtractors, Complementers
    DutUnit("Sub"                  , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("SubC"                 , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
#   DutUnit("SubCZ"                , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # proof failed
    DutUnit("SubV"                 , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
#   DutUnit("SubVZ"                , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # proof failed
    DutUnit("Neg"                  , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("NegC"                 , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("AbsVal"               , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),

    # Adder-Subtractors
    DutUnit("AddSub"               , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("AddSubC"              , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("AddSubV"              , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),

    # Incrementers, Decrementers
    DutUnit("Inc"                  , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("IncC"                 , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("Dec"                  , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("DecC"                 , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("IncDec"               , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("IncDecC"              , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),

    # Comparators
    DutUnit("CmpEQ"                , [                            Timing.FAST]),
    DutUnit("CmpGE"                , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("CmpEQGE"              , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),

    # Multipliers
#   DutUnit("MulSgn"               , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # proof takes a long time
#   DutUnit("MulUns"               , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # equivalence timeout
#   DutUnit("MulAddSgn"            , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
#   DutUnit("MulAddUns"            , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
#   DutUnit("AddMulSgn"            , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # equivalence timeout
#   DutUnit("AddMulUns"            , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # equivalence timeout
#   DutUnit("MulCsvSgn"            , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
#   DutUnit("MulCsvUns"            , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
#   DutUnit("SqrSgn"               , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # ERROR: No SAT model available for cell $flatten\gate.$0 ($pow).
#   DutUnit("SqrUns"               , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # ERROR: No SAT model available for cell $flatten\gate.$0 ($pow).

    # helpers for Sqr*
#   DutUnit("SqrPPGenSgn"          , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral
#   DutUnit("SqrPPGenUns"          , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral

    # helpers
#   DutUnit("MulPPGenSgn"          , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral
#   DutUnit("MulPPGenUns"          , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral
#   DutUnit("AddMulPPGenSgn"       , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral
#   DutUnit("AddMulPPGenUns"       , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral

    # Dividers, Square-Root Extractors
#   DutUnit("DivArrSgn"            , [Timing.SLOW                            ]), # equivalence fail
#   DutUnit("DivArrUns"            , [Timing.SLOW                            ]), # equivalence fail
#   DutUnit("SqrtArrUns"           , [Timing.SLOW                            ]), # ERROR: Feature unimplemented at /home/izi/VLSI/yosys/frontends/slang/lib/src/slang_frontend.cc:799, see AST and code line dump above

    # Detectors
    DutUnit("AllOneDet"            , [                            Timing.FAST]),
    DutUnit("AllZeroDet"           , [                            Timing.FAST]),
    DutUnit("SumZeroDet"           , [                            Timing.FAST]),
    DutUnit("LeadZeroDet"          , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("LeadOneDet"           , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("LeadSignDet"          , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("Log2"                 , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),

    # Encoders, Decoders, Gray
    DutUnit("Decode"               , [                            Timing.FAST]),
    DutUnit("Encode"               , [                            Timing.FAST]),
    DutUnit("Bin2Gray"             , [                            Timing.FAST]),
    DutUnit("Gray2Bin"             , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("IncGray"              , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("IncGrayC"             , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),

    # Miscellaneous
    DutUnit("Cnt"                  , [Timing.SLOW,                Timing.FAST]),
#   DutUnit("Cpr"                  , [Timing.SLOW,                Timing.FAST]), # missing behavioral
    DutUnit("RedAnd"               , [                            Timing.FAST]),
    DutUnit("RedOr"                , [                            Timing.FAST]),
    DutUnit("RedXor"               , [                            Timing.FAST]),
    DutUnit("PrefixAnd"            , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
    DutUnit("PrefixOr"             , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),
#   DutUnit("PrefixAndOr"          , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral
    DutUnit("PrefixXor"            , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),

    # helper for Cnt
#   DutUnit("CntSlice"             , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral

    # helper for many
    DutUnit("FullAdder"            , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]),

    # helper unused
#   DutUnit("Reg"                  , [Timing.SLOW, Timing.MEDIUM, Timing.FAST]), # missing behavioral
]

for unit in units:
    unit_test(unit)
