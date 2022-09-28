const {
  progress_exam_list,
  progress_section_list,
  author_list,
  book_list,
  author_book_map,
} = require('./data');

const example_1 = () => {
  console.time('example_1');
  const new_progress_exam_list = progress_exam_list.map(
    async (progress_exam) => {
      const progress_filters = progress_section_list.filter(
        ({ progress_exam_id }) => progress_exam_id === progress_exam.id
      );
      return {
        ...progress_exam,
        progress_section_list: progress_filters,
      };
    }
  );
  /**
   * Expect Result
   * it to the console.
   */
  //   console.log(JSON.stringify(new_progress_exam_list, null, 2));
  console.timeEnd('example_1');
};

const example_2 = () => {
  console.time('example_2');
  const author_map = author_book_map.map(({ author_id, book_id }) => {
    const author = author_list.find(({ id }) => id === author_id);
    const book = book_list.find(({ id }) => id === book_id);

    return {
      ...book,
      author_list: author,
    };
  });

  const new_book_list = book_list.map((book) =>
    author_map.filter(({ id }) => id === book.id)
  );

  /**
   * Expect Result
   * it to the console.
   */
  //   console.log(JSON.stringify(new_book_list, null, 2));
  console.timeEnd('example_2');
};

(() => {
  example_1();
  example_2();
})();
