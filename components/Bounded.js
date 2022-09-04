import clsx from "clsx";

export const Bounded = ({
  as: Comp = "div",
  size = "base",
  className,
  children,
}) => {
  return (
    // <Comp className={clsx("px-4 py-8 md:py-10 md:px-6 lg:py-12", className)}></Comp>
    <Comp className={clsx("mb-8", className)}>
      <div
        className={clsx(
          "mx-auto w-full",
          size === "small" && "max-w-3xl",
          size === "base" && "max-w-4xl",
          size === "wide" && "max-w-5xl",
          size === "widest" && "max-w-6xl"
        )}
      >
        {children}
      </div>
    </Comp>
  );
};
