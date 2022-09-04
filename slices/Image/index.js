import * as prismicH from "@prismicio/helpers";
import { PrismicNextImage } from "@prismicio/next";

import { Bounded } from "../../components/Bounded";

const Image = ({ slice }) => {
  const image = slice.primary.image;

  return (
    <Bounded as='section' size={slice.variation === "wide" ? "widest" : "base"}>
      <figure className='grid grid-cols-1 gap-2'>
        {prismicH.isFilled.image(image) && (
          <div className='bg-gray-100'>
            <PrismicNextImage field={image} layout='responsive' />
          </div>
        )}
        <figcaption className='overflow-auto font-serif tracking-tight'>
          {/* Left Caption */}
          {prismicH.isFilled.keyText(slice.primary.title) &&
            prismicH.isFilled.keyText(slice.primary.caption) && (
              <span className='float-left inline-block text-sm font-light'>
                <b className='font-bold'>{slice.primary.title}</b>{" "}
                {slice.primary.caption}
              </span>
            )}

          {/* Right Caption */}
          {prismicH.isFilled.keyText(slice.primary.source) && (
            <span className='float-right inline-block text-sm font-light'>
              FOTO {slice.primary.source}
            </span>
          )}
        </figcaption>
      </figure>
    </Bounded>
  );
};

export default Image;
