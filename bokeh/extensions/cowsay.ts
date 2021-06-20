import * as p from "core/properties"
import {pre} from "core/dom"
import {Markup, MarkupView} from "models/widgets/markup"
declare const cowsay: any

export class CowsayPreTextView extends MarkupView  {
  model: CowsayPreText

  render(): void {
    super.render();

    type CowType = keyof typeof cowsay;
    let cow_type: CowType = this.model.cow_type;
    const content = pre({style: {overflow: "auto"}}, cowsay.say({
        text: this.model.text,
        cow: cowsay[cow_type],
    }));
    this.markup_el.appendChild(content);
  }
}

export namespace CowsayPreText {
  export type Attrs = p.AttrsOf<Props>

  export type Props = Markup.Props & {
    cow_type: p.Property<string>
  }
}

export interface CowsayPreText extends CowsayPreText.Attrs {}

export class CowsayPreText extends Markup {
  properties: CowsayPreText.Props
  __view_type__: CowsayPreTextView

  constructor(attrs?: Partial<CowsayPreText.Attrs>) {
    super(attrs)
  }

  static init_CowsayPreText() {
    this.prototype.default_view = CowsayPreTextView    
    this.define<CowsayPreText.Props>(({String}) => ({
      cow_type: [ String ]
    }))
  }
}