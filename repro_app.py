import gradio as gr
import pandas as pd

def on_dataset_change(consulta_type):
    # Simulate different datasets
    if consulta_type == "Dataset 1":
        provincias = ["Prov A", "Prov B"]
    else:
        # Overlapping province to test "stickiness"
        provincias = ["Prov A", "Prov C"]
    
    # We explicitly try to clear with value=None
    print(f"Changing dataset to {consulta_type}, clearing inputs")
    return gr.update(choices=provincias, value=None), gr.update(choices=[], value=None)

def on_provincia_change(provincia):
    print(f"Province changed to: {provincia}")
    if not provincia:
        return gr.update(choices=[], value=None)
    
    # Simulate departments
    dptos = [f"Dept 1 of {provincia}", f"Dept 2 of {provincia}"]
    return gr.update(choices=dptos, value=None)

with gr.Blocks() as app:
    t = gr.Radio(["Dataset 1", "Dataset 2"], label="Tipo de Matrícula", value="Dataset 1")
    p = gr.Dropdown(choices=["Prov A", "Prov B"], label="Provincia")
    d = gr.Dropdown(choices=[], label="Departamento")
    
    # Correctly mimic the outputs order in the real app
    # In real app: outputs=[dataset_state, jurisdiccion, departamento]
    # Here we skip dataset_state for simplicity but keep the structure for dropdowns
    t.change(fn=on_dataset_change, inputs=[t], outputs=[p, d])
    
    p.change(fn=on_provincia_change, inputs=[p], outputs=[d])

if __name__ == "__main__":
    app.launch()
