def obter_template_tela_listagem(nome_componente, tabela, titulo, subtitulo):

    importacoes_reducer = f"""
import {{
  InformacoesIniciais{nome_componente},
  {nome_componente}Action,
  {nome_componente}ActionTypes,
  {nome_componente}State
}} from './{nome_componente}.types';
"""

    return f"""
import {{ useEffect, useReducer, useRef }} from 'react';
import style from './{nome_componente}.module.css';
{importacoes_reducer}
const obterEstadoInicialDaTela = (informacoesIniciais: InformacoesIniciais{nome_componente}): {nome_componente}State => {{
  return {{
    mostrarFiltro: false,
    filtroProps: {{
      cookiesFiltrosVerificados: false,
      qtdFiltrosAplicados: 0,
      queryDefault: ``,
      queryFiltro: "",
    }},
    listagemPD1: {{
      dados: null,
      loading: false,
      semDados: false,
      paginaAtual: 1,
      quantidadeDadosNaPaginaAtual: 0,
      quantidadePaginas: 0,
      query: ``,
    }},
  }};
}};



const reducerTela = (
  state: {nome_componente}State,
  action: {nome_componente}Action
): {nome_componente}State => {{
  switch (action.type) {{
    case {nome_componente}ActionTypes.SETAR_DADOS_LISTAGEM_PD1:
      if (state?.listagemPD1?.dados == action?.listagemPD1) return state;
      return {{
        ...state,
        listagemPD1: {{
          ...state.listagemPD1,
          dados: action.listagemPD1,
          loading: false,
          semDados: action.listagemPD1?.vDados?.length == 0,
          quantidadeDadosNaPaginaAtual: action.listagemPD1?.vDados.length,
          quantidadePaginas: obterQuantidadePaginasListagem(action.listagemPD1),
        }},
      }};

    case {nome_componente}ActionTypes.LOADING_LISTAGEM_PD1:
      if (state?.listagemPD1?.loading == action?.loading) return state;
      return {{
        ...state,
        listagemPD1: {{
          ...state.listagemPD1,
          loading: action.loading,
        }},
      }};

    case {nome_componente}ActionTypes.ALTERAR_FILTRO_PROPS:
      if (state.filtroProps == action.filtroProps) return state;
      return {{
        ...state,
        filtroProps: action.filtroProps,
      }};

    case {nome_componente}ActionTypes.SETAR_QUERY_PD1:
      if (state.listagemPD1.query == action.query) return state;
      return {{
        ...state,
        listagemPD1: {{
          ...state.listagemPD1,
          query: action.query,
          paginaAtual: action.paginaAtual
            ? action.paginaAtual
            : state.listagemPD1.paginaAtual,
        }},
      }};

    case {nome_componente}ActionTypes.MUDAR_PAGINA_ATUAL_PD1:
      if (state.listagemPD1.paginaAtual == action.paginaAtual) return state;
      return {{
        ...state,
        listagemPD1: {{ ...state.listagemPD1, paginaAtual: action.paginaAtual }},
      }};

    case {nome_componente}ActionTypes.MOSTRAR_FILTRO:
      if (state.mostrarFiltro) return state;
      return {{
        ...state,
        mostrarFiltro: true,
      }};

    case {nome_componente}ActionTypes.ESCONDER_FILTRO:
      if (!state.mostrarFiltro) return state;
      return {{
        ...state,
        mostrarFiltro: false,
      }};

    case {nome_componente}ActionTypes.SETAR_QUERY_FILTRO:
      return {{
        ...state,
        filtroProps: action.filtroProps,
      }};

    default:
      return state;
  }}
}};


export default function {nome_componente}() {{
  // Hooks
  const {{
    paramAgrup,
    paramModulo,
    paramMenu,
    paramTabela,
    paramAcao,
  }} = useParametrosTela();

  // Reducer
  const [estadoTela, dispatch] = useReducer(reducerTela, undefined, () => {{
    return obterEstadoInicialDaTela({{}});
  }});

  // API
  const {{ obterListagem }} = useApiListagem();

  // Iniciar componente
  useEffect(() => {{
    iniciarTela();
  }}, []);

  useEffect(() => {{
    fetchListagem{tabela}();
  }}, [estadoTela?.filtroProps?.queryFiltro]);

  const iniciarTela = () => {{
    fetchListagem{tabela}();
  }};

  const reloadTela = () => {{
    fetchListagem{tabela}();
  }};

  const fetchListagem{tabela} = async () => {{
    setLoadingListagem{tabela}(true);
    const listagem{tabela}: Listagem = await obterListagem({{
      pagina: estadoTela?.listagem{tabela}?.paginaAtual,
      tabela: '{tabela}',
      filtros: estadoTela?.filtroProps?.queryFiltro,
      paramMenuTabela: paramMenu.param
    }});
    dispatch({{
      type: {nome_componente}ActionTypes.SETAR_DADOS_LISTAGEM_{tabela},
      listagem{tabela}
    }});
  }};

  const setLoadingListagem{tabela} = (loading: boolean) => {{
    dispatch({{
      type: {nome_componente}ActionTypes.LOADING_LISTAGEM_{tabela},
      loading
    }});
  }};

  const alterarQtdFiltrosAplicados = (qtdFiltrosAplicados: number) => {{
    dispatch({{
      type: {nome_componente}ActionTypes.ALTERAR_FILTRO_PROPS,
      filtroProps: {{
        ...estadoTela.filtroProps,
        qtdFiltrosAplicados
      }}
    }});
  }};

  const setarQuery{tabela} = (query: string) => {{
    dispatch({{
      type: {nome_componente}ActionTypes.SETAR_QUERY_{tabela},
      query,
      paginaAtual: 1
    }});
  }};

  const setarQueryFiltro = (
    novaQuery: string,
    qtdFiltros: number,
    cookiesFiltrosVerificados?: boolean
  ) => {{
    dispatch({{
      type: {nome_componente}ActionTypes.SETAR_QUERY_FILTRO,
      filtroProps: {{
        ...estadoTela.filtroProps,
        queryFiltro: novaQuery,
        qtdFiltrosAplicados: qtdFiltros,
        cookiesFiltrosVerificados: cookiesFiltrosVerificados,
      }},
    }});
  }};


  const handlePaginaAtual = (novaPaginaAtual: number) => {{
    dispatch({{
      type: {nome_componente}ActionTypes.MUDAR_PAGINA_ATUAL_{tabela},
      paginaAtual: novaPaginaAtual
    }});
  }};

  const mostrarFiltro = () => {{
    dispatch({{
      type: TelaListagemTesteActionTypes.MOSTRAR_FILTRO,
    }});
  }};

  const esconderFiltro = () => {{
    dispatch({{
      type: TelaListagemTesteActionTypes.ESCONDER_FILTRO,
    }});
  }};

  return (
    <section className={{style.listagem__box}}>
      <TooltipIndicadores></TooltipIndicadores>
      <FiltroLateralListagemManual
        queryDefault={{estadoTela.filtroProps.queryDefault}}
        setQuantidadeFiltrosAplicados={{alterarQtdFiltrosAplicados}}
        tabela="{tabela}"
        dadosListagem={{estadoTela?.listagem{tabela}?.dados}}
        filtroVisivel={{estadoTela?.mostrarFiltro}}
        esconderFiltro={{esconderFiltro}}
        setQuery={{setarQueryFiltro}}
      ></FiltroLateralListagemManual>
      <Breadcrumb
        items={{[
          {{ label: paramAgrup.descricao, isActive: false }},
          {{ label: paramModulo.modulo, isActive: false }},
          {{ label: paramMenu.menu, isActive: true }}
        ]}}
      />
      <ToolBarTelas
        titulo="{titulo}"
        subTitulo="{subtitulo}"
        quantidadeFiltrosAplicados={{estadoTela?.filtroProps?.qtdFiltrosAplicados}}
        dadosListagem={{estadoTela?.listagem{tabela}?.dados}}
        isBtnIncluir={{true}}
        btnReload={{true}}
        onClickBtnRealod={{reloadTela}}
        isBtnFiltrar={{true}}
        mostrarFiltroLateral={{() => {{
          abrirFecharFiltroLateral(true);
        }}}}
      >
      </ToolBarTelas>
      {{estadoTela?.listagem{tabela}?.loading ? (
        <div className={{style.spinner__listagem}}>
          <Spinner texto='Carregando dados' size='40px' fontSizeTexto='12px'></Spinner>
        </div>
      ) : estadoTela?.listagem{tabela}?.semDados ? (
        <div className={{style.semDadosContainer}}>
          <SemDados height='280px' onClickRecarregar={{fetchListagem{tabela}}}></SemDados>
        </div>
      ) : estadoTela.listagem{tabela}.dados ? (
        <div className={{style?.listagemContainer}}>
          <ListagemTabela
            mostrarInfoTabela={{true}}
            funcaoRecarregarLista={{fetchListagem{tabela}}}
            heightContainer='calc(100vh - 270px)'
            dadosListagem={{estadoTela?.listagem{tabela}?.dados}}
            paginaAtual={{estadoTela?.listagem{tabela}?.paginaAtual}}
            quantidadeDadosNaPaginaAtual={{estadoTela?.listagem{tabela}?.quantidadeDadosNaPaginaAtual}}
            quantidadePaginas={{estadoTela?.listagem{tabela}?.quantidadePaginas}}
            setPaginaAtual={{handlePaginaAtual}}
            paramAgrup={{paramAgrup}}
            paramModulo={{paramModulo}}
            paramMenu={{paramMenu}}
            paramAcao={{paramAcao}}
            paramTabela='{tabela}'
          />
        </div>
      ) : (
        ''
      )}}
    </section>
  );
}}

    """

def obter_template_tela_listagem_types(nome_componente, tabela):
    return f"""
export interface DadosListagem {{
  dados: Listagem;
  loading: boolean;
  semDados: boolean;
  paginaAtual: number;
  quantidadeDadosNaPaginaAtual: number;
  quantidadePaginas: number;
  query: string;
}}

export interface FiltroProps {{
  qtdFiltrosAplicados?: number;
  cookiesFiltrosVerificados?: boolean;
  queryDefault: string;
  queryFiltro: string;
}}

export interface {nome_componente}State {{
  listagem{tabela}: DadosListagem;
  filtroProps: FiltroProps;  
  mostrarFiltro?: boolean;
}}

export interface {nome_componente}Action {{
  type: {nome_componente}ActionTypes;
  listagem{tabela}?: Listagem;
  loading?: boolean;
  linhaSelecionada?: ListagemLinha;
  filtroProps?: FiltroProps;
  query?: string;
  paginaAtual?: number;
}}

export enum {nome_componente}ActionTypes {{
  SETAR_DADOS_LISTAGEM_{tabela} = 'SETAR_DADOS_LISTAGEM_{tabela}',
  LOADING_LISTAGEM_{tabela} = 'LOADING_LISTAGEM_{tabela}',
  MUDAR_PAGINA_ATUAL_{tabela} = 'MUDAR_PAGINA_ATUAL_{tabela}',
  SETAR_QUERY_{tabela} = 'SETAR_QUERY_PROPS',
  ALTERAR_FILTRO_PROPS = 'ALTERAR_FILTRO_PROPS',
  MOSTRAR_FILTRO = "MOSTRAR_FILTRO",
  ESCONDER_FILTRO = "ESCONDER_FILTRO",
}}

export interface InformacoesIniciais{nome_componente} {{
}}
"""

def obter_template_tela_listagem_estilos():
    return """
.spinner {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: calc(100vh - 227px);
}

.spinner__listagem {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: calc(100vh - 210px);
}

.semDadosContainer {
  display: flex;
  align-items: center;
  justify-content: center;
  height: calc(100vh - 210px);
}

.listagemContainer {
  margin-top: 1em;
}
"""
