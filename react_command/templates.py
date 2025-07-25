# def obter_template_arquivo_componente(nome_componente, com_reducer):

#     importacoes_reducer = f"""
# import {{
#   InformacoesIniciais{nome_componente},
#   {nome_componente}Action,
#   {nome_componente}ActionTypes,
#   {nome_componente}State
# }} from './{nome_componente}.types';
# """

#     funcoes_reducer = f"""
# const obterEstadoInicialDaTela = (
#   informacoesIniciais: InformacoesIniciais{nome_componente}
# ): {nome_componente}State => {{
#   return {{
#       }};
# }};

# const reducerTela = (
#   state: {nome_componente}State,
#   action: {nome_componente}Action
# ): {nome_componente}State => {{
#   switch (action.type) {{
#     default:
#       return state;
#   }}
# }};
# """

#     hook_reducer = """
# // Reducer
# const [estadoTela, dispatch] = useReducer(reducerTela, undefined, () => {
#     return obterEstadoInicialDaTela({});
# });
#     """

#     importacao_hook_reducer = ", useReducer"

#     return f"""
# import style from './{nome_componente}.module.css';
# import {{ memo{importacao_hook_reducer if com_reducer else ""} }} from 'react';
# {importacoes_reducer if com_reducer else ""}

# {funcoes_reducer if com_reducer else ""}

# interface Props {{

# }}

# const {nome_componente} = () => {{

#     {hook_reducer if com_reducer else ""}

#     return (

#     )
# }}

# export default memo({nome_componente})
#     """

# def obter_template_arquivo_types(nome_componente, com_reducer):
#     tipos_reducer =  f"""
# export interface {nome_componente}State {{

# }}

# export interface {nome_componente}Action {{
#   type: {nome_componente}ActionTypes;
# }}

# export enum {nome_componente}ActionTypes {{

# }}

# export interface InformacoesIniciais{nome_componente} {{

# }}

# """
#     return tipos_reducer if com_reducer else ""

# def obter_template_arquivo_api(nome_componente):
#     return f"""
# // export default function useApi{nome_componente}() {{
# //   const {{ post }} = useApi<any>();

# //   function method(payload: {{  }}): Promise<any> {{
# //     const apiUrl = Endpoints.;
# //     return post(false, apiUrl, payload);
# //   }}

# //   return {{ method }};
# // }}

#     """

# def obter_template_tela_listagem(nome_componente, tabela, titulo, subtitulo):

#     importacoes_reducer = f"""
# import {{
#   InformacoesIniciais{nome_componente},
#   {nome_componente}Action,
#   {nome_componente}ActionTypes,
#   {nome_componente}State
# }} from './{nome_componente}.types';
# """

#     return f"""
# import {{ useEffect, useReducer, useRef }} from 'react';
# import style from './{nome_componente}.module.css';
# {importacoes_reducer}
# const obterEstadoInicialDaTela = (informacoesIniciais: InformacoesIniciais{nome_componente}): {nome_componente}State => {{
#   return {{
#     filtroProps: {{
#       cookiesFiltrosVerificados: false,
#       mostrarFiltro: false,
#       qtdFiltrosAplicados: 0,
#       queryDefault: ``
#     }},
#     listagem{tabela}: {{
#       dados: null,
#       loading: false,
#       semDados: false,
#       paginaAtual: 1,
#       quantidadeDadosNaPaginaAtual: 0,
#       quantidadePaginas: 0,
#       query: ``
#     }},
#   }};
# }};

# const reducerTela = (state: {nome_componente}State, action: {nome_componente}Action): {nome_componente}State => {{
#   switch (action.type) {{
#     case {nome_componente}ActionTypes.SETAR_DADOS_LISTAGEM_{tabela}:
#       if (state?.listagem{tabela}?.dados == action?.listagem{tabela}) return state;
#       return {{
#         ...state,
#         listagem{tabela}: {{
#           ...state.listagem{tabela},
#           dados: action.listagem{tabela},
#           loading: false,
#           semDados: action.listagem{tabela}?.vDados?.length == 0,
#           quantidadeDadosNaPaginaAtual: action.listagem{tabela}?.vDados.length,
#           quantidadePaginas: obterQuantidadePaginasListagem(action.listagem{tabela})
#         }}
#       }};

#     case {nome_componente}ActionTypes.LOADING_LISTAGEM_{tabela}:
#       if (state?.listagem{tabela}?.loading == action?.loading) return state;
#       return {{
#         ...state,
#         listagem{tabela}: {{
#           ...state.listagem{tabela},
#           loading: action.loading
#         }}
#       }};

#     case {nome_componente}ActionTypes.ALTERAR_FILTRO_PROPS:
#       if (state.filtroProps == action.filtroProps) return state;
#       return {{
#         ...state,
#         filtroProps: action.filtroProps
#       }};

#     case {nome_componente}ActionTypes.SETAR_QUERY_{tabela}:
#       if (state.listagem{tabela}.query == action.query) return state;
#       return {{
#         ...state,
#         listagem{tabela}: {{
#           ...state.listagem{tabela},
#           query: action.query,
#           paginaAtual: action.paginaAtual ? action.paginaAtual : state.listagem{tabela}.paginaAtual
#         }}
#       }};

#     case {nome_componente}ActionTypes.MUDAR_PAGINA_ATUAL_{tabela}:
#       if (state.listagem{tabela}.paginaAtual == action.paginaAtual) return state;
#       return {{ ...state, listagem{tabela}: {{ ...state.listagem{tabela}, paginaAtual: action.paginaAtual }} }};

#     default:
#       return state;
#   }}
# }};

# export default function {nome_componente}() {{
#   // Hooks
#   const {{
#     paramAgrup,
#     paramModulo,
#     paramMenu,
#     paramTabela,
#     paramAcao,
#   }} = useParametrosTela();

#   // Reducer
#   const [estadoTela, dispatch] = useReducer(reducerTela, undefined, () => {{
#     return obterEstadoInicialDaTela({{}});
#   }});

#   // API
#   const {{ obterListagem }} = useApiListagem();

#   // Iniciar componente
#   useEffect(() => {{
#     iniciarTela();
#   }}, []);

#   useEffect(() => {{
#     fetchListagem{tabela}();
#   }}, [estadoTela?.listagem{tabela}?.query]);

#   const iniciarTela = () => {{
#     fetchListagem{tabela}();
#   }};

#   const reloadTela = () => {{
#     fetchListagem{tabela}();
#   }};

#   const fetchListagem{tabela} = async () => {{
#     setLoadingListagem{tabela}(true);
#     const listagem{tabela}: Listagem = await obterListagem({{
#       pagina: estadoTela?.listagem{tabela}?.paginaAtual,
#       tabela: '{tabela}',
#       filtros: estadoTela?.listagem{tabela}?.query,
#       paramMenuTabela: paramMenu.param
#     }});
#     dispatch({{
#       type: {nome_componente}ActionTypes.SETAR_DADOS_LISTAGEM_{tabela},
#       listagem{tabela}
#     }});
#   }};

#   const setLoadingListagem{tabela} = (loading: boolean) => {{
#     dispatch({{
#       type: {nome_componente}ActionTypes.LOADING_LISTAGEM_{tabela},
#       loading
#     }});
#   }};

#   const alterarQtdFiltrosAplicados = (qtdFiltrosAplicados: number) => {{
#     dispatch({{
#       type: {nome_componente}ActionTypes.ALTERAR_FILTRO_PROPS,
#       filtroProps: {{
#         ...estadoTela.filtroProps,
#         qtdFiltrosAplicados
#       }}
#     }});
#   }};

#   const setarQuery{tabela} = (query: string) => {{
#     dispatch({{
#       type: {nome_componente}ActionTypes.SETAR_QUERY_{tabela},
#       query,
#       paginaAtual: 1
#     }});
#   }};

#   const handlePaginaAtual = (novaPaginaAtual: number) => {{
#     dispatch({{
#       type: {nome_componente}ActionTypes.MUDAR_PAGINA_ATUAL_{tabela},
#       paginaAtual: novaPaginaAtual
#     }});
#   }};

#   const abrirFecharFiltroLateral = (abrir: boolean) => {{
#     dispatch({{
#       type: {nome_componente}ActionTypes.ALTERAR_FILTRO_PROPS,
#       filtroProps: {{
#         ...estadoTela.filtroProps,
#         mostrarFiltro: abrir
#       }}
#     }});
#   }};

#   return (
#     <section className={{style.listagem__box}}>
#       <TooltipIndicadores></TooltipIndicadores>
#       <FiltroLateralListagemManual
#         queryDefault={{estadoTela.filtroProps.queryDefault}}
#         setQuantidadeFiltrosAplicados={{alterarQtdFiltrosAplicados}}
#         tabela='{tabela}'
#         dadosListagem={{estadoTela?.listagem{tabela}?.dados}}
#         filtroVisivel={{estadoTela?.filtroProps?.mostrarFiltro}}
#         esconderFiltro={{() => abrirFecharFiltroLateral(false)}}
#         setQuery={{setarQuery{tabela}}}
#       ></FiltroLateralListagemManual>
#       <Breadcrumb
#         items={{[
#           {{ label: paramAgrup.descricao, isActive: false }},
#           {{ label: paramModulo.modulo, isActive: false }},
#           {{ label: paramMenu.menu, isActive: true }}
#         ]}}
#       />
#       <ToolBarTelas
#         titulo="{titulo}"
#         subTitulo="{subtitulo}"
#         quantidadeFiltrosAplicados={{estadoTela?.filtroProps?.qtdFiltrosAplicados}}
#         dadosListagem={{estadoTela?.listagem{tabela}?.dados}}
#         isBtnIncluir={{true}}
#         btnReload={{true}}
#         onClickBtnRealod={{reloadTela}}
#         isBtnFiltrar={{true}}
#         mostrarFiltroLateral={{() => {{
#           abrirFecharFiltroLateral(true);
#         }}}}
#       >
#       </ToolBarTelas>
#       {{estadoTela?.listagem{tabela}?.loading ? (
#         <div className={{style.spinner__listagem}}>
#           <Spinner texto='Carregando dados' size='40px' fontSizeTexto='12px'></Spinner>
#         </div>
#       ) : estadoTela?.listagem{tabela}?.semDados ? (
#         <div className={{style.semDadosContainer}}>
#           <SemDados height='280px' onClickRecarregar={{fetchListagem{tabela}}}></SemDados>
#         </div>
#       ) : estadoTela.listagem{tabela}.dados ? (
#         <div className={{style?.listagemContainer}}>
#           <ListagemTabela
#             mostrarInfoTabela={{true}}
#             funcaoRecarregarLista={{fetchListagem{tabela}}}
#             heightContainer='calc(100vh - 270px)'
#             dadosListagem={{estadoTela?.listagem{tabela}?.dados}}
#             paginaAtual={{estadoTela?.listagem{tabela}?.paginaAtual}}
#             quantidadeDadosNaPaginaAtual={{estadoTela?.listagem{tabela}?.quantidadeDadosNaPaginaAtual}}
#             quantidadePaginas={{estadoTela?.listagem{tabela}?.quantidadePaginas}}
#             setPaginaAtual={{handlePaginaAtual}}
#             paramAgrup={{paramAgrup}}
#             paramModulo={{paramModulo}}
#             paramMenu={{paramMenu}}
#             paramAcao={{paramAcao}}
#             paramTabela='{tabela}'
#           />
#         </div>
#       ) : (
#         ''
#       )}}
#     </section>
#   );
# }}

#     """

# def obter_template_tela_listagem_types(nome_componente, tabela):
#     return f"""
# export interface DadosListagem {{
#   dados: Listagem;
#   loading: boolean;
#   semDados: boolean;
#   paginaAtual: number;
#   quantidadeDadosNaPaginaAtual: number;
#   quantidadePaginas: number;
#   query: string;
# }}

# export interface FiltroProps {{
#   mostrarFiltro?: boolean;
#   qtdFiltrosAplicados?: number;
#   cookiesFiltrosVerificados?: boolean;
#   queryDefault: string;
# }}

# export interface {nome_componente}State {{
#   listagem{tabela}: DadosListagem;
#   filtroProps: FiltroProps;
# }}

# export interface {nome_componente}Action {{
#   type: {nome_componente}ActionTypes;
#   listagem{tabela}?: Listagem;
#   loading?: boolean;
#   linhaSelecionada?: ListagemLinha;
#   filtroProps?: FiltroProps;
#   query?: string;
#   paginaAtual?: number;
# }}

# export enum {nome_componente}ActionTypes {{
#   SETAR_DADOS_LISTAGEM_{tabela} = 'SETAR_DADOS_LISTAGEM_{tabela}',
#   LOADING_LISTAGEM_{tabela} = 'LOADING_LISTAGEM_{tabela}',
#   MUDAR_PAGINA_ATUAL_{tabela} = 'MUDAR_PAGINA_ATUAL_{tabela}',
#   SETAR_QUERY_{tabela} = 'SETAR_QUERY_PROPS',
#   ALTERAR_FILTRO_PROPS = 'ALTERAR_FILTRO_PROPS'
# }}

# export interface InformacoesIniciais{nome_componente} {{
# }}
# """

# def obter_template_tela_listagem_estilos():
#     return """
# .spinner {
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   width: 100%;
#   height: calc(100vh - 227px);
# }

# .spinner__listagem {
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   width: 100%;
#   height: calc(100vh - 210px);
# }

# .semDadosContainer {
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   height: calc(100vh - 210px);
# }

# .listagemContainer {
#   margin-top: 1em;
# }
# """
