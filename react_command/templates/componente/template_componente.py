def obter_template_arquivo_componente(nome_componente, com_reducer):

    importacoes_reducer = f"""
import {{
  InformacoesIniciais{nome_componente},
  {nome_componente}Action,
  {nome_componente}ActionTypes,
  {nome_componente}State
}} from './{nome_componente}.types';
"""

    funcoes_reducer = f"""
const obterEstadoInicialDaTela = (
  informacoesIniciais: InformacoesIniciais{nome_componente}
): {nome_componente}State => {{
  return {{
      }};
}};

const reducerTela = (
  state: {nome_componente}State,
  action: {nome_componente}Action
): {nome_componente}State => {{
  switch (action.type) {{
    default:
      return state;
  }}
}};
"""

    hook_reducer = """
// Reducer
const [estadoTela, dispatch] = useReducer(reducerTela, undefined, () => {
    return obterEstadoInicialDaTela({});
});
    """

    importacao_hook_reducer = ", useReducer"

    return f"""
import style from './{nome_componente}.module.css';
import {{ memo{importacao_hook_reducer if com_reducer else ""} }} from 'react';
{importacoes_reducer if com_reducer else ""}

{funcoes_reducer if com_reducer else ""}

interface Props {{

}}

const {nome_componente} = () => {{

    {hook_reducer if com_reducer else ""}

    return (

    )
}}

export default memo({nome_componente})
    """

def obter_template_arquivo_types(nome_componente, com_reducer):
    tipos_reducer =  f"""
export interface {nome_componente}State {{

}}

export interface {nome_componente}Action {{
  type: {nome_componente}ActionTypes;
}}

export enum {nome_componente}ActionTypes {{

}}

export interface InformacoesIniciais{nome_componente} {{

}}

"""
    return tipos_reducer if com_reducer else ""

def obter_template_arquivo_api(nome_componente):
    return f"""
// export default function useApi{nome_componente}() {{
//   const {{ post }} = useApi<any>();

//   function method(payload: {{  }}): Promise<any> {{
//     const apiUrl = Endpoints.;
//     return post(false, apiUrl, payload);
//   }}

//   return {{ method }};
// }}

    """
