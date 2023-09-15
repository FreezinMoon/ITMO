ORG     	0x420	         ; Адрес начала программы

hlt_command: WORD 0x10
ls_command: WORD 0x18
cla_command: WORD 0xF0
ld_command: WORD 0xA0

buffer_cell: WORD 0
buf_cell_two: WORD 0
zero_cell: WORD 0x0

START:	CLA		; Очистка аккумулятора
S1:		IN 5		; Ожидание ввода названия команды
		AND #0x40; Проверка на наличие введенного символа
		BEQ S1	; Нет - "Спин-луп"
		IN 4		; Ввод байта в AC


		CMP ls_command  ; проверка на совпадение введенного
		BEQ ls_exec     ; символа с имеющимися коммандами

		CMP cla_command
		BEQ cla_exec

		CMP ld_command
		BEQ ld_exec

		CMP hlt_command
		BEQ hlt_exec

		JUMP unknown_exec

ls_exec: 	CLA
			IN 5		; Ожидание ввода аргумента
			AND #0x40; Проверка на наличие введенного символа
			BEQ ls_exec	; Нет - "Спин-луп"
			IN 4		; Ввод байта в AC
			ST buffer_cell ; сохраняем на будущее

			LD #0x3E
			OUT 0xC
			LD #0x20
			OUT 0xC
			LD #0x6C
			OUT 0xC
			LD #0x73
			OUT 0xC
			LD #0x20
			OUT 0xC

			LD buffer_cell
			ST buf_cell_two
			CALL translate

			LD #0x0A
			OUT 0xC

			LD (buffer_cell)
			SWAB
			OUT 0xC
			SWAB
			OUT 0xC
			LD #0x0A
			OUT 0xC
			CLA
			JUMP S1

cla_exec: 	LD #0x3E
			OUT 0xC
			LD #0x20
			OUT 0xC
			LD #0x43
			OUT 0xC
			LD #0x4C
			OUT 0xC
			LD #0x41
			OUT 0xC
			LD #0x0A
			OUT 0xC

			CLA
			ST (zero_cell)
			JUMP S1

ld_exec: 	ST zero_cell
			LD #0x3E
			OUT 0xC
			LD #0x20
			OUT 0xC
			LD #0x4C
			OUT 0xC
			LD #0x44
			OUT 0xC
			LD #0x0A
			OUT 0xC

			CLA
			JUMP S1

hlt_exec: 	LD #0x3E
			OUT 0xC
			LD #0x20
			OUT 0xC
			LD #0x48
			OUT 0xC
			LD #0x4C
			OUT 0xC
			LD #0x54
			OUT 0xC
			LD #0x0A
			OUT 0xC

			HLT

unknown_exec: 	ST buf_cell_two
      		          LD #0x3E
					OUT 0xC
					LD #0x20
					OUT 0xC
					CALL translate
					LD #0x0A
		               OUT 0xC
		               LD #0x4E
		               OUT 0xC
		               LD #0x4F
		               OUT 0xC
		               LD #0x4E
		               OUT 0xC
		               LD #0x45
		               OUT 0xC
		               LD #0x0A
		               OUT 0xC
		               CLA
		               JUMP S1


translate:   LD buf_cell_two
	            ASR
	            ASR
	            ASR
	            ASR
	            AND #0xF
	            CMP #0xA
	            BMI T1
	            ADD #0x37
	            OUT 0xC
	            BPL T2
T1:            ADD #0x30
	            OUT 0xC

T2:            LD buf_cell_two
	            AND #0xF
	            CMP #0xA
	            BMI T3
	            ADD #0x37
	            OUT 0xC
	            BPL T4
T3:	            ADD #0x30
	            OUT 0xC
T4:	            RET


