// Получаем все элементы с атрибутом draggable
let draggables = document.querySelectorAll('[draggable]');

// Добавляем обработчики событий dragstart и dragend для каждого элемента
draggables.forEach(draggable => {
  draggable.addEventListener('dragstart', () => {
    // Добавляем класс dragging к перетаскиваемому элементу
    draggable.classList.add('dragging');
  });

  draggable.addEventListener('dragend', () => {
    // Удаляем класс dragging с перетаскиваемого элемента
    draggable.classList.remove('dragging');
  });
});

// Получаем все элементы с атрибутом droppable
let droppables = document.querySelectorAll('[droppable]');

// Добавляем обработчики событий dragover, dragenter, dragleave и drop для каждого элемента
droppables.forEach(droppable => {
  droppable.addEventListener('dragover', (e) => {
    // Отменяем действие по умолчанию, чтобы разрешить перетаскивание
    e.preventDefault();
    // Получаем элемент, который перетаскивается
    let dragging = document.querySelector('.dragging');
    // Получаем элемент, который находится под курсором
    let afterElement = getDragAfterElement(droppable, e.clientY);
    // Если есть элемент, то вставляем перетаскиваемый элемент после него
    if (afterElement) {
      droppable.insertBefore(dragging, afterElement);
    } else {
      // Иначе вставляем перетаскиваемый элемент в конец списка
      droppable.appendChild(dragging);
    }
  });

  droppable.addEventListener('dragenter', () => {
    // Добавляем класс over к элементу, над которым находится курсор
    droppable.classList.add('over');
  });

  droppable.addEventListener('dragleave', () => {
    // Удаляем класс over с элемента, над которым находится курсор
    droppable.classList.remove('over');
  });

  droppable.addEventListener('drop', () => {
    // Удаляем класс over с элемента, над которым находится курсор
    droppable.classList.remove('over');
  });
});

// Функция, которая возвращает элемент, который находится под курсором
function getDragAfterElement(container, y) {
  // Получаем все элементы в контейнере, кроме перетаскиваемого
  let draggableElements = [...container.querySelectorAll('[draggable]:not(.dragging)')];

  // Возвращаем ближайший элемент по вертикали или null, если нет такого
  return draggableElements.reduce((closest, child) => {
    // Получаем координаты центра элемента
    let box = child.getBoundingClientRect();
    let offset = y - box.top - box.height / 2;
    // Если курсор находится выше центра элемента и расстояние меньше, чем у предыдущего ближайшего элемента, то обновляем ближайший элемент
    if (offset < 0 && offset > closest.offset) {
      return { offset: offset, element: child };
    } else {
      return closest;
    }
  }, { offset: Number.NEGATIVE_INFINITY }).element;
}
