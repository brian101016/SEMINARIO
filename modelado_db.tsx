// #region ##################################################################################### ESSENTIALS
// ---------------------------------------------------------------------- ONLY KEYS
/**
 * Selecciona todas las propiedades de un objeto, sin importar el tipo de dato.
 */
export type OnlyKeys<T> = { [P in keyof T]?: any };

// ---------------------------------------------------------------------- AUTO KEYS
/**
 * Selecciona todas las propiedades y permite agregar nuevas.
 */
export type AutoKeys<T> = OnlyKeys<T> & { [key: string]: any };

// ---------------------------------------------------------------------- _SETUP
/**
 * Clase extensible que coloca `props` automáticamente.
 * 1. {@link id} - ***readonly*** `string | null`.
 */
abstract class _setup {
  /**
   * `string | null` - ID del elemento.
   *
   * Si proviene de `Firestore`, entonces se refiere al ID del documento.
   *
   * Todos los elementos tienen un ID aún si no se necesita.
   * */
  readonly id: string | null = null;

  /**
   * Coloca todos los props automáticamente.
   * @param ini Objeto de donde obtener los datos iniciales.
   *
   * 1. Puede estar vacío y puede omitir algunos campos.
   * 2. Se toma el valor por defecto de las propiedades que no se incluyan.
   * 3. Si el tipo de dato de las propiedades no coincide, se ignora.
   * 4. Se pueden incluir propiedades de más.
   * 5. Si el campo actual es `null`, entonces acepta **cualquier valor** (`null <-- any`).
   * 6. Es **imposible colocar `null`** a un campo que ya exista (`any <-/- null`).
   */
  protected update(ini?: AutoKeys<this>) {
    if (ini === undefined) return;
    for (const key in this) {
      const that = ini[key];
      if (that === undefined || that === null) continue;
      if (
        this[key] === null ||
        (typeof that === typeof this[key] &&
          (typeof that !== "object" ||
            Object.getPrototypeOf(that) === Object.getPrototypeOf(this[key])))
      ) {
        this[key as string] = that;
      }
    }
  }

  /**
   * Coloca todos los props automáticamente.
   * @param ini Objeto de donde obtener los datos iniciales.
   *
   * 1. Puede estar vacío y puede omitir algunos campos.
   * 2. Se toma el valor por defecto de las propiedades que no se incluyan.
   * 3. Si el tipo de dato de las propiedades no coincide, se ignora.
   * 4. Se pueden incluir propiedades de más.
   * 5. Si el campo actual es `null`, entonces acepta **cualquier valor** (`null <-- any`).
   * 6. Es **imposible colocar `null`** a un campo que ya exista (`any <-/- null`).
   */
  constructor(ini?: AutoKeys<_setup>) {
    this.update(ini);
  }
}
// #endregion

// #region ##################################################################################### SACRAMENTOS
// ---------------------------------------------------------------------- SACRAMENTO (base)
/**
 * Contiene información general de cualquier sacramento.
 *
 * 1. {@link id} - ***readonly*** `string | null`.
 * 1. {@link fecha_sacramento} - `Date`.
 * 1. {@link presbitero} - `string`.
 * 1. {@link libro} - `number`.
 * 1. {@link pagina} - `number`.
 * 1. {@link partida} - `number`.
 * 1. {@link notas} - `string`.
 */
export abstract class Sacramento extends _setup {
  /** `Date` - Fecha cuando se ejerció el sacramento. */
  fecha_sacramento: Date = new Date();
  /** `string` - Nombre completo del presbítero a cargo, separado con espacios donde sea necesario. */
  presbitero: string = "";

  /** `number` - Representa el número del libro según el sacramento. */
  libro: number = 0;
  /** `number` - Representa el número de página según el libro. */
  pagina: number = 0;
  /** `number` - Representa el número de partida según la página. */
  partida: number = 0;
  /** `string` - Cualquier consideración o notas adicionales. */
  notas: string = "";

  /**
   * Coloca todos los props automáticamente.
   * @param ini Objeto de donde obtener los datos iniciales.
   *
   * 1. Puede estar vacío y puede omitir algunos campos.
   * 2. Se toma el valor por defecto de las propiedades que no se incluyan.
   * 3. Si el tipo de dato de las propiedades no coincide, se ignora.
   * 4. Se pueden incluir propiedades de más.
   */
  constructor(ini?: AutoKeys<Sacramento>) {
    super(ini);
    this.update(ini);
  }
}

// ---------------------------------------------------------------------- BAUTIZOS
/**
 * Contiene toda la información relevante a los bautismos.
 *
 * 1. {@link id} - ***readonly*** `string | null`.
 * 1. {@link nombre} - `string`.
 * 1. {@link sexo} - `boolean`.
 * 1. {@link fecha_nacimiento} - `Date`.
 * 1. {@link ciudad_nacimiento} - `string`.
 * 1. {@link folio_acta_nacimiento} - `string`.
 * 1. {@link padre} - `string`.
 * 1. {@link madre} - `string`.
 * 1. {@link abuelos_paternos} - `string`.
 * 1. {@link abuelos_maternos} - `string`.
 * 1. {@link padrino} - `string`.
 * 1. {@link madrina} - `string`.
 * 1. {@link notas_marginales} - `string`.
 * 1. {@link fecha_sacramento} - `Date`.
 * 1. {@link presbitero} - `string`.
 * 1. {@link libro} - `number`.
 * 1. {@link pagina} - `number`.
 * 1. {@link partida} - `number`.
 * 1. {@link notas} - `string`.
 */
export class Bautizo extends Sacramento {
  /** `string` - Nombre completo del bebé, separado con espacios donde sea necesario. */
  nombre: string = "";
  /** `boolean` - Sexo del bebé según: `false` para hombre, `true` para mujer. */
  sexo: boolean = false;
  /** `Date` - Fecha de nacimiento del bebé. */
  fecha_nacimiento: Date = new Date();
  /** `string` - Ciudad y lugar de nacimiento. */
  ciudad_nacimiento: string = "";
  /** `string` - Folio del acta de nacimiento según como aparezca en el registro civil. */
  folio_acta_nacimiento: string = "";

  /** `string` - Nombre completo del padre, separado con espacios donde sea necesario. */
  padre: string = "";
  /** `string` - Nombre completo de la madre, separado con espacios donde sea necesario. */
  madre: string = "";
  /** `string` - Nombre completo de los abuelos paternos, separado con espacios y coma donde sea necesario. */
  abuelos_paternos: string = "";
  /** `string` - Nombre completo de los abuelos maternos, separado con espacios y coma donde sea necesario. */
  abuelos_maternos: string = "";
  /** `string` - Nombre completo del padrino, separado con espacios donde sea necesario. */
  padrino: string = "";
  /** `string` - Nombre completo de la madrina, separado con espacios donde sea necesario. */
  madrina: string = "";

  /** `string` - Notas marginales aplicables. */
  notas_marginales: string = "";

  /**
   * Coloca todos los props automáticamente.
   * @param ini Objeto de donde obtener los datos iniciales.
   *
   * 1. Puede estar vacío y puede omitir algunos campos.
   * 2. Se toma el valor por defecto de las propiedades que no se incluyan.
   * 3. Si el tipo de dato de las propiedades no coincide, se ignora.
   * 4. Se pueden incluir propiedades de más.
   */
  constructor(ini?: AutoKeys<Bautizo>) {
    super(ini);
    this.update(ini);
  }
}

// ---------------------------------------------------------------------- COMUNIONES
/**
 * Contiene toda la información relevante a las comuniones.
 *
 * 1. {@link id} - ***readonly*** `string | null`.
 * 1. {@link nombre} - `string`.
 * 1. {@link sexo} - `boolean`.
 * 1. {@link padre} - `string`.
 * 1. {@link madre} - `string`.
 * 1. {@link padrino_madrina} - `string`.
 * 1. {@link ciudad_bautizo} - `string`.
 * 1. {@link parroquia_bautizo} - `string`.
 * 1. {@link fecha_bautizo} - `Date`.
 * 1. {@link fecha_sacramento} - `Date`.
 * 1. {@link presbitero} - `string`.
 * 1. {@link libro} - `number`.
 * 1. {@link pagina} - `number`.
 * 1. {@link partida} - `number`.
 * 1. {@link notas} - `string`.
 */
export class Comunion extends Sacramento {
  /** `string` - Nombre completo de quien recibe el sacramento, separado con espacios donde sea necesario. */
  nombre: string = "";
  /** `boolean` - Sexo del bebé según: `false` para hombre, `true` para mujer. */
  sexo: boolean = false;

  /** `string` - Nombre completo del padre, separado con espacios donde sea necesario. */
  padre: string = "";
  /** `string` - Nombre completo de la madre, separado con espacios donde sea necesario. */
  madre: string = "";
  /** `string` - Nombre completo del padrino o madrina, separado con espacios donde sea necesario. */
  padrino_madrina: string = "";

  /** `string` - Ciudad y lugar donde se recibió el bautismo. */
  ciudad_bautizo: string = "Hermosillo, Sonora";
  /** `string` - Parroquia donde se recibió el bautismo. */
  parroquia_bautizo: string = "";
  /** `Date` - Fecha de cuando se recibió el bautismo. */
  fecha_bautizo: Date = new Date();

  /**
   * Coloca todos los props automáticamente.
   * @param ini Objeto de donde obtener los datos iniciales.
   *
   * 1. Puede estar vacío y puede omitir algunos campos.
   * 2. Se toma el valor por defecto de las propiedades que no se incluyan.
   * 3. Si el tipo de dato de las propiedades no coincide, se ignora.
   * 4. Se pueden incluir propiedades de más.
   */
  constructor(ini?: AutoKeys<Comunion>) {
    super(ini);
    this.update(ini);
  }
}

// ---------------------------------------------------------------------- CONFIRMACIONES
/**
 * Contiene toda la información relevante a las confirmaciones.
 *
 * 1. {@link id} - ***readonly*** `string | null`.
 * 1. {@link nombre} - `string`.
 * 1. {@link sexo} - `boolean`.
 * 1. {@link padre} - `string`.
 * 1. {@link madre} - `string`.
 * 1. {@link padrino_madrina} - `string`.
 * 1. {@link parroquia_bautizo} - `string`.
 * 1. {@link ciudad_bautizo} - `string`.
 * 1. {@link fecha_bautizo} - `Date`.
 * 1. {@link fecha_sacramento} - `Date`.
 * 1. {@link presbitero} - `string`.
 * 1. {@link libro} - `number`.
 * 1. {@link pagina} - `number`.
 * 1. {@link partida} - `number`.
 * 1. {@link notas} - `string`.
 */
export class Confirmacion extends Sacramento {
  /** `string` - Nombre completo de quien recibe el sacramento, separado con espacios donde sea necesario. */
  nombre: string = "";
  /** `boolean` - Sexo según: `false` para hombre, `true` para mujer. */
  sexo: boolean = false;

  /** `string` - Nombre completo del padre, separado con espacios donde sea necesario. */
  padre: string = "";
  /** `string` - Nombre completo de la madre, separado con espacios donde sea necesario. */
  madre: string = "";
  /** `string` - Nombre completo del padrino o madrina, separado con espacios donde sea necesario. */
  padrino_madrina: string = "";

  /** `string` - Parroquia donde se recibió el bautismo. */
  parroquia_bautizo: string = "";
  /** `string` - Ciudad donde se recibió el bautismo. */
  ciudad_bautizo: string = "";
  /** `Date` - Fecha de cuando se recibió el bautismo. */
  fecha_bautizo: Date = new Date();

  /**
   * Coloca todos los props automáticamente.
   * @param ini Objeto de donde obtener los datos iniciales.
   *
   * 1. Puede estar vacío y puede omitir algunos campos.
   * 2. Se toma el valor por defecto de las propiedades que no se incluyan.
   * 3. Si el tipo de dato de las propiedades no coincide, se ignora.
   * 4. Se pueden incluir propiedades de más.
   */
  constructor(ini?: AutoKeys<Confirmacion>) {
    super(ini);
    this.update(ini);
  }
}

// ---------------------------------------------------------------------- MATRIMONIOS
/**
 * Contiene toda la información relevante a los matrimonios.
 *
 * 1. {@link id} - ***readonly*** `string | null`.
 * 1. {@link novio} - `string`.
 * 1. {@link novia} - `string`.
 * 1. {@link domicilio} - `string`.
 * 1. {@link ciudad_sacramento} - `string`.
 * 1. {@link padres_novio} - `string`.
 * 1. {@link padres_novia} - `string`.
 * 1. {@link testigos} - `string[]`.
 * 1. {@link presentacion} - `string`.
 * 1. {@link fecha_sacramento} - `Date`.
 * 1. {@link presbitero} - `string`.
 * 1. {@link libro} - `number`.
 * 1. {@link pagina} - `number`.
 * 1. {@link partida} - `number`.
 * 1. {@link notas} - `string`.
 */
export class Matrimonio extends Sacramento {
  /** `string` - Nombre completo del novio, separado con espacios donde sea necesario. */
  novio: string = "";
  /** `string` - Nombre completo de la novia, separado con espacios donde sea necesario. */
  novia: string = "";

  /** `string` - Domicilio de los novios, anotado en cualquier formato. */
  domicilio: string = "";
  /** `string` - Ciudad donde se recibió el sacramento en custión. */
  ciudad_sacramento: string = "";

  /** `string` - Nombre completo de los padres del novio, separado con espacios y una coma donde sea necesario. */
  padres_novio: string = "";
  /** `string` - Nombre completo de los padres de la novia, separado con espacios y una coma donde sea necesario. */
  padres_novia: string = "";

  /** `string[]` - Lista de testigos del matrimonio. Nombre completo de los testigos, separado con espacios donde sea necesario. */
  testigos: string[] = [];
  /** `string` - Presentación matrimonial o anotaciones particulares. */
  presentacion: string = "";

  /**
   * Coloca todos los props automáticamente.
   * @param ini Objeto de donde obtener los datos iniciales.
   *
   * 1. Puede estar vacío y puede omitir algunos campos.
   * 2. Se toma el valor por defecto de las propiedades que no se incluyan.
   * 3. Si el tipo de dato de las propiedades no coincide, se ignora.
   * 4. Se pueden incluir propiedades de más.
   */
  constructor(ini?: AutoKeys<Matrimonio>) {
    super(ini);
    this.update(ini);
  }
}
// #endregion
