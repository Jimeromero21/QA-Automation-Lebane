
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from helpers import login_helper


def test_empezar_proyecto_nuevo(driver):
    wait = WebDriverWait(driver, 15)

    # Paso 1: iniciar sesión
    login_helper(driver)

    # Paso 2: validar la página principal
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(., 'Buenos días')]")
        )
    )

    # Paso 3: abrir el formulario de proyecto
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(normalize-space(), 'Agregar proyecto')]")
        )
    ).click()

    # Paso 4: validar la URL
    wait.until(
        EC.url_to_be("https://tst.lebane.app/primer-proyecto")
    )
    assert driver.current_url == "https://tst.lebane.app/primer-proyecto"

    # Paso 5: validar el título
    titulo = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[normalize-space()='PROYECTO']")
        )
    )
    assert titulo.is_displayed()

    # Paso 6: completar el nombre
   
    # Paso 6: completar el nombre con un valor único
    nombre = wait.until(
        EC.visibility_of_element_located((By.NAME, "nombreProyecto"))
    )

    nombre_proyecto = (
        "Proyecto QA Automatizado "
        + datetime.now().strftime("%Y%m%d_%H%M%S")
    )

    nombre.clear()
    nombre.send_keys(nombre_proyecto)

    print("Nombre del proyecto:", nombre_proyecto)


    # Paso 7: seleccionar moneda ARS
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-cy="new-renderer-field-moneda"]')
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@role='option' and normalize-space(.)='ARS']")
        )
    ).click()

    wait.until(
        lambda d: d.find_element(
            By.CSS_SELECTOR, '[data-cy="new-renderer-field-moneda"]'
        ).get_attribute("value") == "ARS"
    )
    print("Moneda ARS seleccionada correctamente")

    # Paso 8: seleccionar Argentina
    # Se vuelve a localizar el campo en cada intento de espera.
    pais_selector = (
        By.CSS_SELECTOR, '[data-cy="new-renderer-field-pais"]'
    )
    wait.until(
        lambda d: d.find_element(*pais_selector).is_enabled()
        and d.find_element(*pais_selector).is_displayed()
    )
    driver.find_element(*pais_selector).click()

    selector_argentina = (
        By.XPATH,
        "//*[@role='option' and "
        "translate(normalize-space(.), "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz')='argentina']"
    )
    wait.until(
        EC.element_to_be_clickable(selector_argentina)
    ).click()
    print("País Argentina seleccionado correctamente")

    # Paso 9: seleccionar provincia Buenos Aires
    provincia_selector = (
        By.CSS_SELECTOR, '[data-cy="new-renderer-field-estado"]'
    )
    wait.until(
        EC.element_to_be_clickable(provincia_selector)
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@role='option' and normalize-space(.)='Buenos Aires']")
        )
    ).click()
    print("Provincia Buenos Aires seleccionada correctamente")

    # Paso 10: seleccionar ciudad La Plata
    ciudad_selector = (
        By.CSS_SELECTOR, '[data-cy="new-renderer-field-ciudad"]'
    )
    wait.until(
        EC.element_to_be_clickable(ciudad_selector)
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@role='option' and normalize-space(.)='La Plata']")
        )
    ).click()
    print("Ciudad La Plata seleccionada correctamente")

    # Paso 11: completar la dirección
    calle = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-cy="new-renderer-field-calle"]')
        )
    )
    calle.clear()
    calle.send_keys("Calle 12")

    numero = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-cy="new-renderer-field-numeroPuerta"]')
        )
    )
    numero.clear()
    numero.send_keys("1234")
    print("Dirección completada correctamente")

    
   
    # Paso 12: seleccionar tipo de construcción Edificio
    tipo_construccion = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-cy="new-renderer-field-tipoConstruccion"]')
        )
    )
    tipo_construccion.click()

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@role='option' and normalize-space(.)='Edificio']")
        )
    ).click()

    print("Tipo de construcción Edificio seleccionado correctamente")

    # Paso 13: seleccionar modalidad de ajuste Provisorio
    modalidad = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-cy="new-renderer-field-modalidadAjuste"]')
        )
    )
    modalidad.click()

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@role='option' and normalize-space(.)='Provisorio']")
        )
    ).click()

    print("Modalidad de ajuste Provisorio seleccionada correctamente")

   
    # Paso 14: completar fecha de fin
    fecha_fin = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[data-cy="new-renderer-field-fechaFin"]')
        )
    )
    fecha_fin.click()
    fecha_fin.send_keys("31122026")

    print("Fecha de fin completada:", fecha_fin.get_attribute("value"))

    # Paso 15: buscar la empresa de prueba
    empresa = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input[placeholder="Escribí para buscar o crear"]')
        )
    )
    empresa.click()
    empresa.send_keys("Empresa QA Automatizada 1792609745160")

    # Paso 16: seleccionar la opción encontrada
    empresa_opcion = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//*[@role='option' and contains(normalize-space(.), 'Empresa QA Automatizada 1792609745160')]"
            )
        )
    )
    empresa_opcion.click()

    print("Empresa seleccionada correctamente")

    # Paso 17: verificar el estado del botón Registrar
    boton_registrar = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[normalize-space()='Registrar']")
        )
    )

    print("Botón Registrar habilitado:", boton_registrar.is_enabled())

    # Paso 18: registrar el proyecto
    assert boton_registrar.is_enabled(), (
        "El botón Registrar debería estar habilitado"
    )

    boton_registrar.click()
    print("Se hizo clic en Registrar")

    
   
    # Paso 19: esperar la respuesta de la aplicación
    wait.until(
        lambda d: "/proyecto/" in d.current_url
        and "/primer-proyecto" not in d.current_url
    )

    print("La aplicación respondió al registro")
    print("URL después de registrar:", driver.current_url)

    # Paso 20: validar que el proyecto se haya creado
    assert "/proyecto/" in driver.current_url, (
        "No se redirigió a la página del proyecto creado"
    )

    confirmacion = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[normalize-space()='Creación exitosa']"
            )
        )
    )

    assert confirmacion.is_displayed(), (
        "No se encontró el mensaje de creación exitosa"
    )

    print("Proyecto creado correctamente")
    print("Nombre del proyecto:", nombre_proyecto)
    print("URL del proyecto:", driver.current_url)
