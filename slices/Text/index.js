import * as prismicH from "@prismicio/helpers";
import { PrismicRichText } from "@prismicio/react";

import { Bounded } from "../../components/Bounded";

const Text = ({ slice }) => {
  return (
    <Bounded as='section'>
      {prismicH.isFilled.richText(slice.primary.text) && (
        <div className='font-serif text-base leading-relaxed md:text-lg md:leading-relaxed'>
          <PrismicRichText field={slice.primary.text} />
        </div>
      )}
    </Bounded>
  );
};

export default Text;
