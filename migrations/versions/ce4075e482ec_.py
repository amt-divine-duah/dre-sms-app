"""empty message

Revision ID: ce4075e482ec
Revises: 9ecee5e65df3
Create Date: 2022-05-08 05:43:54.877223

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ce4075e482ec'
down_revision = '9ecee5e65df3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('reg_date', sa.String(length=80), nullable=True),
    sa.Column('mobile_no', sa.String(length=80), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.Column('admission_no', sa.String(length=80), nullable=True),
    sa.Column('birth_date', sa.String(length=80), nullable=True),
    sa.Column('student_id', sa.String(length=80), nullable=True),
    sa.Column('student_class', sa.String(length=80), nullable=True),
    sa.Column('religion', sa.String(length=80), nullable=True),
    sa.Column('nationality', sa.String(length=80), nullable=True),
    sa.Column('father_name', sa.String(length=80), nullable=True),
    sa.Column('mother_name', sa.String(length=80), nullable=True),
    sa.Column('father_occ', sa.String(length=80), nullable=True),
    sa.Column('mother_occ', sa.String(length=80), nullable=True),
    sa.Column('father_email', sa.String(length=80), nullable=True),
    sa.Column('mother_email', sa.String(length=80), nullable=True),
    sa.Column('father_mobile_no', sa.String(length=80), nullable=True),
    sa.Column('mother_mobile_no', sa.String(length=80), nullable=True),
    sa.Column('present_add', sa.Text(), nullable=True),
    sa.Column('permanent_add', sa.Text(), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_students_student_id'), 'students', ['student_id'], unique=False)
    op.drop_index('ix_student_student_id', table_name='student')
    op.drop_table('student')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('reg_date', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('mobile_no', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('admission_no', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('birth_date', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('student_id', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('student_class', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('religion', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('nationality', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('father_name', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('mother_name', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('father_occ', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('mother_occ', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('father_email', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('mother_email', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('father_mobile_no', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('mother_mobile_no', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('present_add', mysql.TEXT(), nullable=True),
    sa.Column('permanent_add', mysql.TEXT(), nullable=True),
    sa.Column('course_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('department_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('about_me', mysql.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name='student_ibfk_2'),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], name='student_ibfk_3'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='student_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_student_student_id', 'student', ['student_id'], unique=False)
    op.drop_index(op.f('ix_students_student_id'), table_name='students')
    op.drop_table('students')
    # ### end Alembic commands ###