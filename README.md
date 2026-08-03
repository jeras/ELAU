# Library of Arithmetic Units

SystemVerilog Edition!

Based on the [VHDL library](https://iis-people.ee.ethz.ch/~zimmi/arith_lib.html#library) written by Reto Zimmermann.

The library contains various arithmetic operations with multiple architectural choices for different speed requirements. All operations are parametrized in width and performance grade.

## Disclaimer

This project is still under active development; some parts may not yet be fully functional, and existing interfaces, toolflows, and conventions may be broken without prior notice. We target a stable release as soon as possible.

## License

All code checked into this repository is licensed under the permissive Solderpad Hardware License 0.51 (See `LICENSE`).

## Available Operations

### Adders

| Name                                | Description                                       | unsigned | signed | slow | medium | fast |
| ----------------------------------- | ------------------------------------------------- | :------: | :----: | :--: | :----: | :--: |
| [Add](         src/Add.sv         ) | Adder                                             |    X     |   X    |  S   |   M    |  F   |
| [AddC](        src/AddC.sv        ) | Adder with carry-in, carry-out                    |    X     |        |  S   |   M    |  F   |
| [AddCfast](    src/AddCfast.sv    ) | Adder with fast carry-in, carry-out               |    X     |        |  S   |   M    |  F   |
| [AddV](        src/AddV.sv        ) | Adder with carry-in, 2’s compl. overflow flag     |          |   X    |  S   |   M    |  F   |
| [AddMod2Nm1](  src/AddMod2Nm1.sv  ) | Adder modulo 2^n - 1 (double zero representation) |    X     |        |  S   |   M    |  F   |
| [AddMod2Nm1s0](src/AddMod2Nm1s0.sv) | Adder modulo 2^n - 1 (single zero representation) |    X     |        |  S   |   M    |  F   |
| [AddMod2Np1](  src/AddMod2Np1.sv  ) | Adder modulo 2^n + 1                              |    X     |        |  S   |   M    |  F   |
| [AddCsv](      src/AddCsv.sv      ) | Carry-save adder (3 operands)                     |    X     |   X    |      |        |  F   |
| [AddMop](      src/AddMop.sv      ) | Multi-operand adder                               |    X     |   X    |  S   |   M    |  F   |
| [AddMopCsv](   src/AddMopCsv.sv   ) | Carry-save multi-operand adder                    |    X     |   X    |  S   |        |  F   |

### Subtractors, Complementers

| Name                     | Description                                           | unsigned | signed | slow | medium | fast |
| ------------------------ | ----------------------------------------------------- | :------: | :----: | :--: | :----: | :--: |
| [Sub](    src/Sub.sv   ) | Subtractor                                            |    X     |   X    |  S   |   M    |  F   |
| [SubC](   src/SubC.sv  ) | Subtractor with carry-in, carry-out                   |    X     |        |  S   |   M    |  F   |
| [SubCZ](  src/SubCZ.sv ) | Subtractor with carry-in, carry-out, zero flag        |    X     |        |  S   |   M    |  F   |
| [SubV](   src/SubV.sv  ) | Subtractor with carry-in, 2’s compl. overflow flag    |          |   X    |  S   |   M    |  F   |
| [SubVZ](  src/SubVZ.sv ) | Subtractor with carry-in, 2’s compl. ovl. & zero flag |          |   X    |  S   |   M    |  F   |
| [Neg](    src/Neg.sv   ) | 2’s complementer (negation)                           |          |   X    |  S   |   M    |  F   |
| [NegC](   src/NegC.sv  ) | 2’s complementer, conditional                         |          |   X    |  S   |   M    |  F   |
| [AbsVal]( src/AbsVal.sv) | Absolute value for 2’s complement numbers             |          |   X    |  S   |   M    |  F   |

### Adder-Subtractors

| Name                      | Description                                          | unsigned | signed | slow | medium | fast |
| ------------------------- | ---------------------------------------------------- | :------: | :----: | :--: | :----: | :--: |
| [AddSub]( src/AddSub.sv ) | Adder-subtractor                                     |    X     |   X    |  S   |   M    |  F   |
| [AddSubC](src/AddSubC.sv) | Adder-subtractor with carry-in, carry-out            |    X     |        |  S   |   M    |  F   |
| [AddSubV](src/AddSubV.sv) | Adder-subtractor with carry-in, 2’s compl. ovl. flag |          |   X    |  S   |   M    |  F   |

### Incrementers, Decrementers

| Name                      | Description                                      | unsigned | signed | slow | medium | fast |
| ------------------------- | ------------------------------------------------ | :------: | :----: | :--: | :----: | :--: |
| [Inc](    src/Inc.sv    ) | Incrementer                                      |    X     |   X    |  S   |   M    |  F   |
| [IncC](   src/IncC.sv   ) | Incrementer with carry-in, carry-out             |    X     |        |  S   |   M    |  F   |
| [Dec](    src/Dec.sv    ) | Decrementer                                      |    X     |   X    |  S   |   M    |  F   |
| [DecC](   src/DecC.sv   ) | Decrementer with carry-in, carry-out             |    X     |        |  S   |   M    |  F   |
| [IncDec]( src/IncDec.sv ) | Incrementer-decrementer                          |    X     |   X    |  S   |   M    |  F   |
| [IncDecC](src/IncDecC.sv) | Incrementer-decrementer with carry-in, carry-out |    X     |        |  S   |   M    |  F   |

### Comparators

| Name                       | Description                       | unsigned | signed | slow | medium | fast |
| -------------------------- | --------------------------------- | :------: | :----: | :--: | :----: | :--: |
| [CmpEQ](   src/CmpEQ.sv  ) | Equality comparator               |    X     |   X    |      |        |  F   |
| [CmpGE](   src/CmpGE.sv  ) | Magnitude comparator              |    X     |        |  S   |   M    |  F   |
| [CmpEQGE]( src/CmpEQGE.sv) | Equality and magnitude comparator |    X     |   X    |  S   |   M    |  F   |

### Multipliers

| Name                          | Description                    | unsigned | signed | slow | medium | fast |
| ----------------------------- | ------------------------------ | :------: | :----: | :--: | :----: | :--: |
| [MulSgn](   src/MulSgn.sv   ) | Signed multiplier              |          |   X    |  S   |   M    |  F   |
| [MulUns](   src/MulUns.sv   ) | Unsigned multiplier            |    X     |        |  S   |   M    |  F   |
| [MulAddSgn](src/MulAddSgn.sv) | Signed multiplier-adder        |          |   X    |  S   |   M    |  F   |
| [MulAddUns](src/MulAddUns.sv) | Unsigned multiplier-adder      |    X     |        |  S   |   M    |  F   |
| [AddMulSgn](src/AddMulSgn.sv) | Signed adder-multiplier        |          |   X    |  S   |   M    |  F   |
| [AddMulUns](src/AddMulUns.sv) | Unsigned adder-multiplier      |    X     |        |  S   |   M    |  F   |
| [MulCsvSgn](src/MulCsvSgn.sv) | Signed carry-save multiplier   |          |   X    |  S   |        |  F   |
| [MulCsvUns](src/MulCsvUns.sv) | Unsigned carry-save multiplier |    X     |        |  S   |        |  F   |
| [SqrSgn](   src/SqrSgn.sv   ) | Signed squarer                 |          |   X    |  S   |   M    |  F   |
| [SqrUns](   src/SqrUns.sv   ) | Unsigned squarer               |    X     |        |  S   |   M    |  F   |

### Dividers, Square-Root Extractors

| Name                            | Description                          | unsigned | signed | slow | medium | fast |
| ------------------------------- | ------------------------------------ | :------: | :----: | :--: | :----: | :--: |
| [DivArrSgn]( src/DivArrSgn.sv ) | Signed array divider                 |          |   X    |  S   |        |      |
| [DivArrUns]( src/DivArrUns.sv ) | Unsigned array divider               |    X     |        |  S   |        |      |
| [SqrtArrUns](src/SqrtArrUns.sv) | Unsigned array square-root extractor |    X     |        |  S   |        |      |

### Detectors

| Name                              | Description                          | unsigned | signed | slow | medium | fast |
| --------------------------------- | ------------------------------------ | :------: | :----: | :--: | :----: | :--: |
| [AllZeroDet]( src/AllZeroDet.sv ) | All-zeroes detector                  |          |        |      |        |  F   |
| [AllOneDet](  src/AllOneDet.sv  ) | All-ones detector                    |          |        |      |        |  F   |
| [SumZeroDet]( src/SumZeroDet.sv ) | Unsigned array square-root extractor |    X     |   X    |      |        |  F   |
| [LeadZeroDet](src/LeadZeroDet.sv) | Leading-zeroes detector (LZD)        |    X     |        |  S   |   M    |  F   |
| [LeadOneDet]( src/LeadOneDet.sv ) | Leading-ones detector (LOD)          |    X     |        |  S   |   M    |  F   |
| [LeadSignDet](src/LeadSignDet.sv) | Leading-signs detector (LSD)         |          |   X    |  S   |   M    |  F   |
| [Log2](       src/Log2.sv       ) | Integer logarithm (base 2)           |    X     |        |  S   |   M    |  F   |

### Encoders, Decoders, Gray

| Name                        | Description                    | slow | medium | fast |
| --------------------------- | ------------------------------ | :--: | :----: | :--: |
| [Decode](  src/Decode.sv  ) | Decoder                        |      |        |  F   |
| [Encode](  src/Encode.sv  ) | Encoder                        |      |        |  F   |
| [Bin2Gray](src/Bin2Gray.sv) | Binary-to-Gray converter       |      |        |  F   |
| [Gray2Bin](src/Gray2Bin.sv) | Gray-to-binary converter       |  S   |   M    |  F   |
| [IncGray]( src/IncGray.sv ) | Gray incrementer               |  S   |   M    |  F   |
| [IncGrayC](src/IncGrayC.sv) | Gray incrementer with carry-in |  S   |   M    |  F   |

### Miscellaneous

| Name                              | Description      | slow | medium | fast |
| --------------------------------- | ---------------- | :--: | :----: | :--: |
| [Cnt](        src/Cnt.sv        ) | (m,k)-counter    |  S   |        |  F   |
| [Cpr](        src/Cpr.sv        ) | (m,2)-compressor |  S   |        |  F   |
| [RedAnd](     src/RedAnd.sv     ) | Reduce-AND       |      |        |  F   |
| [RedOr](      src/RedOr.sv      ) | Reduce-OR        |      |        |  F   |
| [RedXor](     src/RedXor.sv     ) | Reduce-XOR       |      |        |  F   |
| [PrefixAnd](  src/PrefixAnd.sv  ) | Prefix-AND       |  S   |   M    |  F   |
| [PrefixOr](   src/PrefixOr.sv   ) | Prefix-OR        |  S   |   M    |  F   |
| [PrefixAndOr](src/PrefixAndOr.sv) | Prefix-AND-OR    |  S   |   M    |  F   |
| [PrefixXor](  src/PrefixXor.sv  ) | Prefix-XOR       |  S   |   M    |  F   |
