USE [ENEM_2023]
GO

/****** Object:  Table [dbo].[DadosEscola]    Script Date: 17/08/2024 11:04:15 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[DadosEscola]') AND type in (N'U'))
DROP TABLE [dbo].[DadosEscola]
GO

/****** Object:  Table [dbo].[DadosEscola]    Script Date: 17/08/2024 11:04:15 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[DadosEscola](
	[CO_MUNICIPIO_ESC] [bigint] NULL,
	[NO_MUNICIPIO_ESC] [varchar](32) NULL,
	[CO_UF_ESC] [int] NULL,
	[SG_UF_ESC] [varchar](2) NULL,
	[TP_DEPENDENCIA_ADM_ESC] [varchar](9) NULL,
	[TP_LOCALIZACAO_ESC] [varchar](6) NULL,
	[TP_SIT_FUNC_ESC] [varchar](33) NULL
) 
GO


