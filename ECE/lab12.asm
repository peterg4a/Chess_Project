.ORIG x3000

    LEA R0, CHAR0MSG
    PUTS
    GETC
    ST R0, CHAR0
    LEA R0, CHAR0MSG
    PUTS
    GETC
    ST R0, CHAR1
    LEA R0, CHAR0MSG
    PUTS
    GETC
    ST R0, CHARART

    ;R0 - CHAR0
    LD R0, CHAR0
    LD R1, CHAR1
    LD R2, CHARART
    ;R1 - CHAR1
    ;R2 - CHARART
    ;R3 - ARRAY
    LD R3, ARRAY
    ;R4 - SCREEN
    LD R4, SCREEN
    ;R5 - TEMP
    ;R6 - TEMP
    ;R7 - TEMP

;----------------------------------------------------------------------------
;Fill screen with 0 Chars
    LD R5, HEIGHT
HLOOP
    LD R6, WIDTH
WLOOP
    STR R0, R4, #0  ;writing the 0char
    ADD R4, R4, #1  ;increase screen
    ADD R6, R6, #-1
    BRp WLOOP

    ADD R5, R5, #-1
    BRp HLOOP

;----------------------------------------------------------------------------
; get charart location in the ARRAY
    ADD R2, R2, R2  ; multiply ascii value of CHARART by 16
    ADD R2, R2, R2
    ADD R2, R2, R2
    ADD R2, R2, R2
    ADD R3, R3, R2  ; add that value to ARRAY


;----------------------------------------------------------------------------
; filling in the 1chars at the proper places
    LD R4, SCREEN   ;reset screen
    LD R5, HEIGHT
PROCESS_ROW
    LD R6, WIDTH
    LDR R0, R3, #0  ; load bit line into R0
    BRz NEXTBIT ; end process if row is all 0
    LD R2, BITMASK  ; initialize bitmask to 0000 0000 0000 0001 in R2
PROCESS_BIT
    AND R0, R7, R2  ; extract bit using bitmask
    BRz NEXTBIT     ; bit is 0

; bit is 1
    STR R1, R4, #0  ; store char1 into the current screen location
NEXTBIT
    ADD R2, R2, R2  ; logical shift left of bitmask
    ADD R4, R4, #1  ; increment screen
    ADD R6, R6, #-1  ; decrease width
    BRp PROCESS_BIT

    LD R2, BITMASK  ; reset bitmask
    ADD R4, R4, #1  ; increment screen
    ADD R5, R5, #-1  ; decrease height
    BRp PROCESS_ROW

;----------------------------------------------------------------------------
    LD R4, SCREEN   ;reset screen
    LD R5, Height
PRINT_ROW
    LD R6, WIDTH
PRINT_LETTER
    ADD R0, R4, #0
    PUTS
    ADD R6, R6, #-1
    BRp PRINT_LETTER

    LD R0, RETURN
    OUT
    ADD R5, R5, #-1
    BRp PRINT_ROW

    HALT

;DATA
CHAR0MSG .STRINGZ "Enter the character for 0 : "
CHAR1MSG .STRINGZ "\nEnter the character for 1 : "
CHARARTMSG .STRINGZ "\nEnter the character of the pixle map"
CHAR0 .BLKW 1
CHAR1 .BLKW 1
CHARART .BLKW 1
ARRAY .FILL x4000
SCREEN .FILL x9000
HEIGHT .FILL #16
WIDTH .FILL #16
BITMASK .FILL x0001
RETURN .FILL x0A

.END