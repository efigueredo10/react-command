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