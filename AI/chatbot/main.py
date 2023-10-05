import panel as pn
from utils import get_completion_from_messages, read_content

context = [{'role':'system', 'content':read_content()}]
pn.extension(template="material", theme="dark")
panels = []


def collect_messages(_):
    prompt = user_input.value_input
    user_input.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('Usuario:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Asistente:', pn.pane.Markdown(
            response, width=600,
        )))
    return pn.Column(*panels)


user_input = pn.widgets.TextInput(
    value="Hola",
    placeholder='Ingresa tu texto aquí...',
)
button = pn.widgets.Button(
    name="Enviar!",
    button_type="primary",
)
conversation = pn.bind(
    collect_messages,
    button,
)
dashboard = pn.Column(
    user_input,
    pn.Row(button),
    pn.panel(conversation, loading_indicator=True, height=300),
)
pn.state.template.param.update(title="AyudaEnPython - ChatBot")

pn.panel(dashboard).servable()
