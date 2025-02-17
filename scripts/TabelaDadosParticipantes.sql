USE [ENEM_2023]
GO

/****** Object:  Table [dbo].[DadosParticipantes]    Script Date: 17/08/2024 11:11:08 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[DadosParticipantes]') AND type in (N'U'))
DROP TABLE [dbo].[DadosParticipantes]
GO

/****** Object:  Table [dbo].[DadosParticipantes]    Script Date: 17/08/2024 11:11:08 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[DadosParticipantes](
	[NU_INSCRICAO] [bigint] NULL,
	[NU_ANO] [bigint] NULL,
	[TP_FAIXA_ETARIA] [varchar](18) NULL,
	[TP_SEXO] [varchar](9) NULL,
	[TP_ESTADO_CIVIL] [varchar](39) NULL,
	[TP_COR_RACA] [varchar](13) NULL,
	[TP_NACIONALIDADE] [varchar](13) NULL,
	[TP_ST_CONCLUSAO] [varchar](52) NULL,
	[TP_ANO_CONCLUIU] [varchar](52) NULL,
	[TP_ESCOLA] [varchar](43) NULL,
	[TP_ENSINO] [varchar](43) NULL,
	[IN_TREINEIRO] [varchar](3) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO


