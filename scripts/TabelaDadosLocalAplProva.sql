USE [ENEM_2023]
GO

/****** Object:  Table [dbo].[DadosAplicacaoProva]    Script Date: 17/08/2024 11:24:01 ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[DadosAplicacaoProva]') AND type in (N'U'))
DROP TABLE [dbo].[DadosAplicacaoProva]
GO

/****** Object:  Table [dbo].[DadosAplicacaoProva]    Script Date: 17/08/2024 11:24:01 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[DadosLocalAplProva](
	[CO_MUNICIPIO_PROVA] [bigint] NULL,
	[NO_MUNICIPIO_PROVA] [varchar](30) NULL,
	[CO_UF_PROVA] [bigint] NULL,
	[SG_UF_PROVA] [varchar](2) NULL
)
GO


