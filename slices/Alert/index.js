import React from "react";
import * as prismicH from "@prismicio/helpers";
import clsx from "clsx";
import { PrismicRichText } from "@prismicio/react";

import { Bounded } from "../../components/Bounded";

const Alert = ({ slice }) => (
  <Bounded as='section' size='base'>
    <div className='mt-8 mb-8 border-t-8 border-red bg-red-light px-8 py-8 font-brandon font-normal'>
      {slice.primary.title && (
        <span className='mb-8 block text-2xl font-black uppercase text-red'>
          {slice.primary.title}
        </span>
      )}
      {prismicH.isFilled.richText(slice.primary.description) && (
        <div className={clsx("text-base md:text-lg")}>
          <PrismicRichText field={slice.primary.description} />
        </div>
      )}
    </div>
  </Bounded>
);

export default Alert;
