import argparse
from pydantic import BaseModel, EmailStr, ValidationError, field_validator
import sys

# 🎯 Modelo Pydantic v2
class Usuario(BaseModel):
    nombre: str
    edad: int
    correo: EmailStr

    # 🧠 Validación extra opcional (ejemplo): capitalizar nombre
    @field_validator("nombre")
    @classmethod
    def capitalizar_nombre(cls, v):
        return v.title().strip()

    # Validación de edad en rango permitido
    @field_validator("edad")
    @classmethod
    def validar_rango_edad(cls, v):
        if not (0 < v < 130):
            raise ValueError("La edad debe estar entre 1 y 129")
        return v

def main():
    # 🎯 1. Capturar argumentos con argparse
    parser = argparse.ArgumentParser(description="Registro de usuario")
    parser.add_argument("--nombre", type=str, required=True, help="Tu nombre")
    parser.add_argument("--edad", type=int, required=True, help="Tu edad")
    args = parser.parse_args()

    # 📥 2. Input interactivo
    correo = input("Introduce tu correo electrónico: ").strip()

    # ✅ 3. Validación con Pydantic
    try:
        usuario = Usuario(nombre=args.nombre, edad=args.edad, correo=correo)
        print("\n✅ Registro exitoso:")
        print(usuario.model_dump_json(indent=4))
    except ValidationError as e:
        print("\n❌ Error de validación:")
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
