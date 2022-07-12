from ctypes import cdll, c_int

def start():
    import os
    # get handle from DLL
    Handle_HL = cdll.LoadLibrary(os.getcwd() + "/so/64/libEpsonFiscalInterface.so")

    # connect
    Handle_HL.ConfigurarVelocidad(c_int(115200).value)
    Handle_HL.ConfigurarPuerto("serial:/dev/ttyUSB0")
    error = Handle_HL.Conectar()
    print("Connect: ", error)
    return Handle_HL

def closeX():
    Handle_HL = start()

    error = Handle_HL.ImprimirCierreX()
    print("Cashier receipt: ", error)

    """ Problema
    Integer ObtenerRespuesta( [out] String buffer_salida,
                               Integer largo_buffer_salida,
                               [out] Integer largo_final_buffer_salida )
    Si solo paso el [out] tengo error de buffer:
    Espacio insuficiente en el buffer de salida a fin de rellenar con la información de la respuesta del comando.
    Si le asigno un buffer, 200 por ejemplo, obtengo el error:
    Segmentation Fault """
    command_out = ""
    response = Handle_HL.ObtenerRespuesta(command_out)
    print("Response: ", response, " Command out: ", command_out)

    disconnect = Handle_HL.Desconectar()
    print("Disconnect: ", disconnect)

def getPrinterStatus():
    Handle_HL = start()

    error = Handle_HL.ObtenerEstadoImpresora()
    print("Printer status: ", error)

    command_out = ""
    response = Handle_HL.ObtenerRespuesta(command_out)
    print("Response: ", response, " Command out: ", command_out)

    disconnect = Handle_HL.Desconectar()
    print("Disconnect: ", disconnect)

def getIvaResponsability():
    first_command_out = ""
    Handle_HL = start()

    error = Handle_HL.ConsultarTipoResponsabilidadAnteElIVA(first_command_out, 200)
    print("Error: ", error, "Iva responsability: ", first_command_out)

    command_out = ""
    response = Handle_HL.ObtenerRespuesta(command_out)
    print("Response: ", response, " Command out: ", command_out)

    disconnect = Handle_HL.Desconectar()
    print("Disconnect: ", disconnect)

closeX()
# getIvaResponsability()
# getPrinterStatus()

